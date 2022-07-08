from silx.gui import qt
from silx.gui.plot import Plot1D
import numpy as np

from mainWindowUi import mainWindowUi

import tango
import requests
import pandas as pd

class mainWindow(mainWindowUi):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)

        self.sys_on_button.clicked.connect(self.set_connectionn)
        self.calib_apply_button.clicked.connect(self.apply_calib)
        self.armButton.clicked.connect(self.fh_arm)
        # self.run_button.clicked.connect(self.fh_run)
        # self.plot_button.clicked.connect(self.plot_it)
        # self.data_button.clicked.connect(self.download_data)

    def download_data(self):
        URL = "http://160.103.33.50:8000/data/raw_data/raw_data.h5"
        response = requests.get(URL, verify=False)
        with open('./data/raw_data.h5', 'wb') as f:
            f.write(response.content)

    def plot_it(self):
        fpath = './data/raw_data.h5'
        df = pd.read_hdf(fpath, key='dataset')
        chan_num = 6 # self._ai_params.high_channel - self._ai_params.low_channel + 1
        one_chan_len = int(len(df) / chan_num)
        multi_index = pd.MultiIndex.from_product([list(range(one_chan_len)), list(range(chan_num))])
        df.index = multi_index
        df = df.unstack()
        df.columns = df.columns.droplevel()
        df = df[[0, 1, 2, 3, 4, 5]]
        self.plot.addCurve(list(range(len(df[0]))), df[0])

    def set_connectionn(self):
        self.device = tango.DeviceProxy('NanoControl/NanoControl/1')
        self.device.set_timeout_millis(10000000)
        self.device.set_connection()
    
    def apply_calib(self):
        self.device.apply_calibration()

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
        print(self.time_table, self.temp_table)
        # time = list(map(float, self.time_input.text().split(',')))
        # temp = list(map(float, self.temp_input.text().split(',')))
        self.device.set_fh_time_profile(self.time_table)
        self.device.set_fh_temp_profile(self.temp_table) 
        self.device.arm_fast_heat()

    def fh_run(self):
        self.device.run_fast_heat()