from silx.gui import qt
from silx.gui.plot import Plot1D

from mainWindowUi import mainWindowUi

import tango
import requests
import pandas as pd

class mainWindow(mainWindowUi):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)

        self.sys_on_button.clicked.connect(self.set_connectionn)
        self.calib_apply_button.clicked.connect(self.apply_calib)
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
        # self.device.init_device()
        self.device.set_timeout_millis(10000000)
        self.device.set_connection()
    
    def apply_calib(self):
        self.device.apply_calibration()

    def fh_arm(self):
        time = list(map(float, self.time_input.text().split(',')))
        temp = list(map(float, self.temp_input.text().split(',')))
        self.device.set_fh_time_profile(time)
        self.device.set_fh_temp_profile(temp) 
        self.device.arm_fast_heat()

    def fh_run(self):
        self.device.run_fast_heat()