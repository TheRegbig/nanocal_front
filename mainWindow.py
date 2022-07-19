from silx.gui import qt
from silx.gui.plot import Plot1D
import numpy as np

from mainWindowUi import mainWindowUi
from settings import *
from constants import *

import tango
import requests
import pandas as pd
import json
import os

class mainWindow(mainWindowUi):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)

        try:
            self.settings = SettingsParser(SETTINGS_FILE_REL_PATH).get_params()
        except:
            error_view = qt.QMessageBox()
            error_text = "Settings file is missing or corrupted!"
            error_view.setText(error_text)
            error_view.setWindowTitle("Error")
            error_view.setIcon(qt.QMessageBox.Critical)
            error_view.addButton(qt.QMessageBox.Ok)
            error_view.exec()
            quit()
        
        self.TANGO_HOST = self.settings.tango_host
        self.DEVICE_PROXY= self.settings.device_proxy
        self.HTTP_HOST = self.settings. http_host
        self.DATA_PATH = self.settings.data_path
        self.CALIB_PATH = self.settings.calib_path

        try:
            self.device = tango.DeviceProxy(self.DEVICE_PROXY)
        except:
            error_view = qt.QMessageBox()
            error_text = "No connection to the device! Check proxy in settings."
            error_view.setText(error_text)
            error_view.setWindowTitle("Error")
            error_view.setIcon(qt.QMessageBox.Critical)
            error_view.addButton(qt.QMessageBox.Ok)
            error_view.exec()

        if not os.path.exists(self.DATA_PATH):
            error_view = qt.QMessageBox()
            error_text = "Incorrect data path specified. It will be set to ./data/"
            error_view.setText(error_text)
            error_view.setWindowTitle("Warning")
            error_view.setIcon(qt.QMessageBox.Warning)
            error_view.addButton(qt.QMessageBox.Ok)
            error_view.exec()
            if not os.path.exists('./data/'):
                os.makedirs('./data/')
            self.DATA_PATH = os.path.abspath('./data/')
        self.sysDataPathInput.setText(os.path.abspath(self.DATA_PATH))
        self.sysDataPathInput.setCursorPosition(0)

        if os.path.exists(self.CALIB_PATH):
            self.calibPathInput.setText(os.path.abspath(self.CALIB_PATH))
            self.calibPathInput.setCursorPosition(0)
        else:
            error_view = qt.QMessageBox()
            error_text = "Incorrect calibration file specified. It will be set to default calibration"
            error_view.setText(error_text)
            error_view.setWindowTitle("Warning")
            error_view.setIcon(qt.QMessageBox.Warning)
            error_view.addButton(qt.QMessageBox.Ok)
            error_view.exec()
            self.calibPathInput.setText('select calibration file!')

        self.sysOnButton.clicked.connect(self.set_connection)
        self.sysOffButton.clicked.connect(self.disconnect)
        self.sysDataPathButton.clicked.connect(self.select_data_path)
        self.sysHelpButton.clicked.connect(self.show_help)

        self.calibPathButton.clicked.connect(self.select_calibration_file)
        self.calibViewButton.clicked.connect(self.view_calibraton_info)
        self.calibApplyButton.clicked.connect(self.apply_calib)
        self.armButton.clicked.connect(self.fh_arm)
        self.startButton.clicked.connect(self.fh_run)

    def set_connection(self):
        try:
            self.device.set_timeout_millis(10000000)
            self.device.set_connection()
            [item.setEnabled(True) for item in [self.experimentBox, self.controlTab]]
        except:
            error_view = qt.QMessageBox()
            error_text = "No connection to the device! Check settings and logs."
            error_view.setText(error_text)
            error_view.setWindowTitle("Error")
            error_view.setIcon(qt.QMessageBox.Critical)
            error_view.addButton(qt.QMessageBox.Ok)
            error_view.exec()

    
    def disconnect(self):
        self.device.disconnect()
        [item.setEnabled(False) for item in [self.experimentBox, self.controlTab]]
    
    def select_data_path(self):
        dpath = qt.QFileDialog.getExistingDirectory(self, "Choose folder to save experiment files", \
                                                    None, qt.QFileDialog.ShowDirsOnly)
        self.sysDataPathInput.setText(os.path.abspath(dpath))
        self.sysDataPathInput.setCursorPosition(0)

    def show_help(self):
        self.help_view = qt.QMessageBox()
        info_blob = self.device.get_info[1]
        info_values = []
        for item in info_blob:
            info_values.append(item['value'])
        info_text = 'Developer: {}\nContact: {} \nModel: {} \nVersion: {}\n'.format(*info_values)
        self.help_view.setText(info_text)
        self.help_view.setWindowTitle("Help")
        self.help_view.setIcon(qt.QMessageBox.Information)

        self.help_view.addButton(qt.QMessageBox.Ok)
        self.help_view.exec_()
    # ===================================
    # Calibration   

    def select_calibration_file(self):
        fname = qt.QFileDialog.getOpenFileName(self, "Choose calibration file", None, "*.json")[0]
        self.calibPathInput.setText(os.path.abspath(fname))
        self.calibPathInput.setCursorPosition(0)

    def apply_calib(self):
        with open(self.calibPathInput.text(), 'r') as f:
            raw_calib = json.load(f)
            str_calib = json.dumps(raw_calib)
            self.device.load_calibration(str_calib)
            self.device.apply_calibration()

    def view_calibraton_info(self):
        # change to window with normal information
        self.calib_view = qt.QMessageBox()
        self.calib_view.setText(str(self.device.get_calibration_comment[1][0]['value']))
        self.calib_view.setWindowTitle("Calibration info:")
        self.calib_view.setIcon(qt.QMessageBox.Question)

        reset_button = self.calib_view.addButton('Reset', qt.QMessageBox.ActionRole)
        reset_button.clicked.disconnect()
        reset_button.clicked.connect(self.apply_default_calib)
        self.calib_view.addButton(qt.QMessageBox.Ok)
        self.calib_view.exec_()
    
    def apply_default_calib(self):
        self.device.apply_default_calibration()
        self.calib_view.setText(str(self.device.get_calibration_comment[1][0]['value']))
        self.calibPathInput.setText('default calibration')

    # ===================================
    # Fast heating

    def fh_arm(self):
        xOption = 1000 if self.experimentTimeComboBox.currentIndex()==1 else 1    #0 - time in ms, 1 - time in s
        yOption = self.experimentTempComboBox.currentIndex() #index 0 - temp in C, 1 - volt in V
        uncorrectedProfile = np.array([[],[]], dtype=float)
        for i in range(self.experimentTable.rowCount()):
            uncorrectedProfile = np.hstack((uncorrectedProfile,
                                            [[float(self.experimentTable.item(i, 0).text())],
                                            [float(self.experimentTable.item(i, 1).text())]]))
        correctedProfile = uncorrectedProfile[:, :(np.argmax(uncorrectedProfile[0])+1)]
        correctedProfile = np.insert(correctedProfile, 0, 0, axis=1)
        self.time_table = xOption*correctedProfile[0] # changing s to ms if needed
        self.temp_table = correctedProfile[1]
        
        self.progressBar.setValue(0)  
        self.controlTabsWidget.setCurrentIndex(1) 
        self.progPlot.clear()
        
        y_label = self.experimentTempComboBox.currentText()
        x_label = self.experimentTimeComboBox.currentText()
        self.progPlot.addCurve(x=self.time_table, y=self.temp_table)
        self.progPlot.getXAxis().setLabel(x_label)
        self.progPlot.getYAxis().setLabel(y_label)
        # time = list(map(float, self.time_input.text().split(',')))
        # temp = list(map(float, self.temp_input.text().split(',')))
        self.device.set_fh_time_profile(self.time_table)
        self.device.set_fh_temp_profile(self.temp_table) 
        self.device.arm_fast_heat()

    def _fh_download_data(self):
        URL = self.HTTP_HOST+"data/raw_data/raw_data.h5"
        response = requests.get(URL, verify=False)
        with open('./data/raw_data.h5', 'wb') as f:
            f.write(response.content)

    def _fh_plot_data(self):
        fpath = './data/raw_data.h5'
        df = pd.read_hdf(fpath, key='dataset')
        chan_num = 6 # self._ai_params.high_channel - self._ai_params.low_channel + 1
        one_chan_len = int(len(df) / chan_num)
        multi_index = pd.MultiIndex.from_product([list(range(one_chan_len)), list(range(chan_num))])
        df.index = multi_index
        df = df.unstack()
        df.columns = df.columns.droplevel()
        df = df[[0, 1, 2, 3, 4, 5]]
        self.resultPlot.addCurve(list(range(len(df[0]))), df[0])

    def fh_run(self):
        self.mainTabWidget.setCurrentIndex(1) 
        self.device.run_fast_heat()
        self._fh_download_data()
        self._fh_plot_data()

