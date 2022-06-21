from silx.gui import qt
from silx.gui.plot import Plot1D
from silx.gui import icons

class mainWindowUi(qt.QWidget):
    def __init__(self, parent=None):
        super(mainWindowUi, self).__init__(parent)
        self.setWindowTitle("Nanocontol")
        self.setMinimumHeight(750)

        mainLayout = qt.QHBoxLayout()
        self.setLayout(mainLayout)

        short_button_width = 50
        short_label_width = 30
        long_button_width = 100
        long_label_width = 60
        button_height = 20
        line_input_height = 20
        font = qt.QFont()
        ####### Left control panel
        ########################################
        lcp_width = 200

        leftLayout = qt.QVBoxLayout()
        mainLayout.addLayout(leftLayout)

        ####### System Group Box
        ########################################
        systemBox = qt.QGroupBox("System")
        leftLayout.addWidget(systemBox, 0)
        lout_0 = qt.QVBoxLayout()
        systemBox.setLayout(lout_0)

        lout_1 = qt.QHBoxLayout()
        lout_0.addLayout(lout_1)
        self.sys_on_button = qt.QPushButton("ON")
        self.sys_on_button.setSizePolicy(qt.QSizePolicy.Expanding, qt.QSizePolicy.Expanding)
        font.setBold(True)
        self.sys_on_button.setFont(font)
        lout_1.addWidget(self.sys_on_button, 1)
        self.sys_off_button = qt.QPushButton("OFF")
        self.sys_off_button.setSizePolicy(qt.QSizePolicy.Expanding, qt.QSizePolicy.Expanding)
        font.setBold(True)
        self.sys_off_button.setFont(font)
        lout_1.addWidget(self.sys_off_button, 1)
        self.sys_help_button = qt.QPushButton()
        self.sys_help_button.setIcon(icons.getQIcon('zoom'))
        self.sys_help_button.setToolTip("Help")
        lout_1.addWidget(self.sys_help_button, 0)
        # lout_1.addStretch()
        # lout_2 = qt.QVBoxLayout()
        # lout_1.addLayout(lout_2)
        # self.sys_setup_button = qt.QPushButton("Setup")
        # #self.sys_setup_button.setMinimumWidth(short_button_width)
        # #self.sys_setup_button.setMinimumHeight(button_height)
        # lout_2.addWidget(self.sys_setup_button)
        # self.sys_help_button = qt.QPushButton("Help")
        # #self.sys_help_button.setMinimumWidth(short_button_width)
        # #self.sys_help_button.setMinimumHeight(button_height)
        # lout_2.addWidget(self.sys_help_button)
        # lout_2.setSpacing(1)
        lout_1.setSpacing(1)

        # lout_1 = qt.QVBoxLayout()
        # lout_0.addLayout(lout_1)
        # lout_1.setSpacing(0)
        # lout_1.addWidget(qt.QLabel("Data"))
        # lout_2 = qt.QHBoxLayout()
        # lout_2.setSpacing(0)
        # lout_1.addLayout(lout_2)
        # self.sys_data_path = qt.QLineEdit()
        # self.sys_data_path.setMinimumHeight(line_input_height)
        # self.sys_data_path.setFrame(False)
        # lout_2.addWidget(self.sys_data_path)
        # self.sys_data_path_button = qt.QToolButton(text="...")
        # lout_2.addWidget(self.sys_data_path_button)

        
        # ####### Experiment Group Box
        # ########################################
        # experimentBox = qt.QGroupBox("Experiment")
        # experimentBox.setMinimumWidth(lcp_width)
        # experimentBox.setMinimumHeight(400)
        # leftLayout.addWidget(experimentBox, 0)
        # lout_0 = qt.QVBoxLayout()
        # experimentBox.setLayout(lout_0)

        # lout_1 = qt.QVBoxLayout()
        # lout_0.addLayout(lout_1)
        # lout_1.setSpacing(3)
        # lout_1.addWidget(qt.QLabel("Calibration"))
        # lout_2 = qt.QHBoxLayout()
        # lout_1.addLayout(lout_2)
        # self.calib_path = qt.QLineEdit()
        # self.calib_path.setFrame(False)
        # self.calib_path.setMinimumHeight(line_input_height)
        # lout_2.addWidget(self.calib_path)
        # self.calib_path_button = qt.QToolButton(text="...")
        # self.calib_path_button.setMinimumHeight(button_height)
        # lout_2.addWidget(self.calib_path_button)
        # lout_3 = qt.QHBoxLayout()
        # lout_3.setSpacing(1)
        # lout_1.addLayout(lout_3)
        # lout_3.addStretch()
        # self.calib_view_button = qt.QPushButton("View")
        # self.calib_view_button.setMinimumWidth(short_button_width)
        # self.calib_view_button.setMinimumHeight(button_height)
        # lout_3.addWidget(self.calib_view_button)
        # self.calib_apply_button = qt.QPushButton("Apply")
        # self.calib_apply_button.setMinimumWidth(short_button_width)
        # self.calib_apply_button.setMinimumHeight(button_height)
        # lout_3.addWidget(self.calib_apply_button)

        # lout_0.addStretch()
        # hline = qt.QFrame()
        # hline.setFrameShape(qt.QFrame.HLine)
        # hline.setStyleSheet("color: rgb(220, 220, 220);")
        # lout_0.addWidget(hline)
        # lout_0.addStretch()

        # lout_1 = qt.QVBoxLayout()
        # lout_0.addLayout(lout_1)
        # lout_1.setSpacing(3)
        # lout_1.addWidget(qt.QLabel("Scan"))
        # lout_2 = qt.QHBoxLayout()
        # lout_1.addLayout(lout_2)
        # lout_2.setSpacing(1)
        # lout_2.addStretch()
        # lout_2.addWidget(qt.QLabel("Sample rate:"))
        # self.scanSampleRateInput = qt.QLineEdit()
        # self.scanSampleRateInput.setFrame(False)
        # self.scanSampleRateInput.setFixedWidth(50)
        # self.scanSampleRateInput.setMinimumHeight(line_input_height)
        # lout_2.addWidget(self.scanSampleRateInput)
        # unit = qt.QLabel("Hz")
        # unit.setFixedWidth(20)
        # lout_2.addWidget(unit)
        # lout_3 = qt.QHBoxLayout()
        # lout_1.addLayout(lout_3)
        # lout_3.setSpacing(1)
        # lout_3.addStretch()
        # self.resetScanSampleRateButton = qt.QPushButton("Reset")
        # self.resetScanSampleRateButton.setMinimumWidth(short_button_width)
        # self.resetScanSampleRateButton.setMinimumHeight(button_height)
        # lout_3.addWidget(self.resetScanSampleRateButton)
        # self.applyScanSampleRateButton = qt.QPushButton("Apply")
        # self.applyScanSampleRateButton.setMinimumWidth(short_button_width)
        # self.applyScanSampleRateButton.setMinimumHeight(button_height)
        # lout_3.addWidget(self.applyScanSampleRateButton)

        # lout_0.addStretch()
        # hline = qt.QFrame()
        # hline.setFrameShape(qt.QFrame.HLine)
        # hline.setStyleSheet("color: rgb(220, 220, 220);")
        # lout_0.addWidget(hline)
        # lout_0.addStretch()

        # lout_1 = qt.QVBoxLayout()
        # lout_0.addLayout(lout_1)
        # lout_1.setSpacing(3)
        # lout_1.addWidget(qt.QLabel("Modulation"))
        # lout_2 = qt.QHBoxLayout()
        # lout_1.addLayout(lout_2)
        # lout_2.setSpacing(1)
        # lout_2.addStretch()
        # lout_2.addWidget(qt.QLabel("Frequency:"))
        # self.freqInput = qt.QLineEdit()
        # self.freqInput.setMinimumHeight(line_input_height)
        # self.freqInput.setFrame(False)
        # self.freqInput.setFixedWidth(50)
        # lout_2.addWidget(self.freqInput)
        # units = qt.QLabel("Hz")
        # units.setFixedWidth(20)
        # lout_2.addWidget(units)
        # lout_3 = qt.QHBoxLayout()
        # lout_1.addLayout(lout_3)
        # lout_3.setSpacing(1)
        # lout_3.addStretch()
        # lout_3.addWidget(qt.QLabel("Amplitude:"))
        # self.amplitudeInput = qt.QLineEdit()
        # self.amplitudeInput.setMinimumHeight(line_input_height)
        # self.amplitudeInput.setFixedWidth(50)
        # self.amplitudeInput.setFrame(False)
        # lout_3.addWidget(self.amplitudeInput)
        # units = qt.QLabel("mA")
        # units.setFixedWidth(20)
        # lout_3.addWidget(units)
        # lout_4 = qt.QHBoxLayout()
        # lout_1.addLayout(lout_4)
        # lout_4.setSpacing(1)
        # lout_4.addStretch()
        # lout_4.addWidget(qt.QLabel("Offset:"))
        # self.offsetInput = qt.QLineEdit()
        # self.offsetInput.setMinimumHeight(line_input_height)
        # self.offsetInput.setFixedWidth(50)
        # self.offsetInput.setFrame(False)
        # lout_4.addWidget(self.offsetInput)
        # units = qt.QLabel("mA")
        # units.setFixedWidth(20)
        # lout_4.addWidget(units)
        # lout_5 = qt.QHBoxLayout()
        # lout_1.addLayout(lout_5)
        # lout_5.setSpacing(1)
        # lout_5.addStretch()
        # self.resetModulationParamsButton = qt.QPushButton("Reset")
        # self.resetModulationParamsButton.setMinimumWidth(short_button_width)
        # self.resetModulationParamsButton.setMinimumHeight(button_height)
        # lout_5.addWidget(self.resetModulationParamsButton)
        # self.applyModulationParamsButton = qt.QPushButton("Apply")
        # self.applyModulationParamsButton.setMinimumWidth(short_button_width)
        # self.applyModulationParamsButton.setMinimumHeight(button_height)
        # lout_5.addWidget(self.applyModulationParamsButton)

        # lout_0.addStretch()
        # hline = qt.QFrame()
        # hline.setFrameShape(qt.QFrame.HLine)
        # hline.setStyleSheet("color: rgb(220, 220, 220);")
        # lout_0.addWidget(hline)
        # lout_0.addStretch()

        # lout_1 = qt.QHBoxLayout()
        # lout_0.addLayout(lout_1)
        # lout_1.setSpacing(1)
        # lout_1.addStretch()
        # self.loadConfigButton = qt.QPushButton("Load config")
        # self.loadConfigButton.setMinimumWidth = long_button_width
        # lout_1.addWidget(self.loadConfigButton)
        # self.saveConfigButton = qt.QPushButton("Save config")
        # self.saveConfigButton.setMinimumWidth = long_button_width
        # lout_1.addWidget(self.saveConfigButton)
        # lout_1.addStretch()

        # lout_0.addStretch()

        leftLayout.addStretch(2)

        # ####### Logo
        # ########################################
        lout_0 = qt.QVBoxLayout()
        leftLayout.addLayout(lout_0, 0)
        logo = qt.QLabel()
        logo.setAlignment(qt.Qt.AlignHCenter)
        pixmap = qt.QPixmap("./res/logo.png").scaledToWidth(long_button_width)
        logo.setPixmap(pixmap)
        lout_0.addWidget(logo)
        sign = qt.QLabel("Nanocontrol v.0.1")
        sign.setAlignment(qt.Qt.AlignHCenter)
        lout_0.addWidget(sign)


        # ####### Right experiment main view
        # ########################################
        rightLayout = qt.QVBoxLayout()
        mainLayout.addLayout(rightLayout, 1)

        self.mainTabWidget = qt.QTabWidget()
        self.controlTab = qt.QWidget()
        self.mainTabWidget.addTab(self.controlTab, "Control")
        self.resultTab = qt.QWidget()
        self.mainTabWidget.addTab(self.resultTab, "Result")
        rightLayout.addWidget(self.mainTabWidget)
        
        # # Control tab
        # lout_0 = qt.QVBoxLayout()
        # self.controlTab.setLayout(lout_0)
        # lout_1 = qt.QHBoxLayout()
        # lout_0.addLayout(lout_1)
        
        # lout_1.addWidget(qt.QGroupBox("Prog"))
        # self.controlWidget = qt.QTabWidget()
        # self.signalsTab = qt.QWidget()
        # self.controlWidget.addTab(self.signalsTab, "Signals")
        # self.progTab = qt.QWidget()
        # self.controlWidget.addTab(self.progTab, "Program")
        # lout_1.addWidget(self.controlWidget)
        # lout_2 = qt.QVBoxLayout()
        # self.signalsTab.setLayout(lout_2)
        # lout_2.addWidget(Plot1D())
        # lout_3 = qt.QVBoxLayout()
        # self.progTab.setLayout(lout_3)
        # lout_3.addWidget(Plot1D())

        # valuesBox = qt.QGroupBox("Values")
        # lout_0.addWidget(valuesBox)
        # lout_1 = qt.QHBoxLayout()
        # valuesBox.setLayout(lout_1)
        # lout_1.addStretch()
        # lout_1.addStretch()

        # lout_2 = qt.QVBoxLayout()
        # lout_1.addLayout(lout_2)
        # lout_2_1 = qt.QHBoxLayout()
        # lout_2.addLayout(lout_2_1)
        # labl = qt.QLabel("R htr abs:")
        # labl.setAlignment(qt.Qt.AlignRight)
        # labl.setMinimumWidth(long_label_width)
        # lout_2_1.addWidget(labl)
        # self.rhtrabsValueLabel = qt.QLabel("0.00")
        # self.rhtrabsValueLabel.setFixedWidth(short_label_width)
        # self.rhtrabsValueLabel.setAlignment(qt.Qt.AlignLeft)
        # lout_2_1.addWidget(self.rhtrabsValueLabel)
        # lout_2_2 = qt.QHBoxLayout()
        # lout_2.addLayout(lout_2_2)
        # labl = qt.QLabel("R htr dyn:")
        # labl.setAlignment(qt.Qt.AlignRight)
        # labl.setMinimumWidth(long_label_width)
        # lout_2_2.addWidget(labl)
        # self.rhtrdynValueLabel = qt.QLabel("0.00")
        # self.rhtrdynValueLabel.setFixedWidth(short_label_width)
        # self.rhtrdynValueLabel.setAlignment(qt.Qt.AlignLeft)
        # lout_2_2.addWidget(self.rhtrdynValueLabel)
        # lout_2_3 = qt.QHBoxLayout()
        # lout_2.addLayout(lout_2_3)
        # labl = qt.QLabel("U mod htr:")
        # labl.setAlignment(qt.Qt.AlignRight)
        # labl.setMinimumWidth(long_label_width)
        # lout_2_3.addWidget(labl)
        # self.umodhtrValueLabel = qt.QLabel("0.00")
        # self.umodhtrValueLabel.setFixedWidth(short_label_width)
        # self.umodhtrValueLabel.setAlignment(qt.Qt.AlignLeft)
        # lout_2_3.addWidget(self.umodhtrValueLabel)
        # lout_2_4 = qt.QHBoxLayout()
        # lout_2.addLayout(lout_2_4)
        # labl = qt.QLabel("I htr:")
        # labl.setAlignment(qt.Qt.AlignRight)
        # labl.setMinimumWidth(long_label_width)
        # lout_2_4.addWidget(labl)
        # labl.setAlignment(qt.Qt.AlignRight)
        # lout_2_4.addWidget(labl)
        # self.ihtrValueLabel = qt.QLabel("0.00")
        # self.ihtrValueLabel.setFixedWidth(short_label_width)
        # self.ihtrValueLabel.setAlignment(qt.Qt.AlignLeft)
        # lout_2_4.addWidget(self.ihtrValueLabel)

        # lout_1.addStretch()
        # vline = qt.QFrame()
        # vline.setFrameShape(qt.QFrame.VLine)
        # vline.setStyleSheet("color: rgb(220, 220, 220);")
        # lout_1.addWidget(vline)
        # lout_1.addStretch()

        # lout_2 = qt.QVBoxLayout()
        # lout_1.addLayout(lout_2)
        # lout_2_1 = qt.QHBoxLayout()
        # lout_2.addLayout(lout_2_1)
        # labl = qt.QLabel("T aux:")
        # labl.setAlignment(qt.Qt.AlignRight)
        # labl.setMinimumWidth(long_label_width)
        # lout_2_1.addWidget(labl)
        # self.tauxValueLabel = qt.QLabel("0.00")
        # self.tauxValueLabel.setFixedWidth(short_label_width)
        # self.tauxValueLabel.setAlignment(qt.Qt.AlignLeft)
        # lout_2_1.addWidget(self.tauxValueLabel)
        # lout_2_2 = qt.QHBoxLayout()
        # lout_2.addLayout(lout_2_2)
        # labl = qt.QLabel("T tpl:")
        # labl.setAlignment(qt.Qt.AlignRight)
        # labl.setMinimumWidth(long_label_width)
        # lout_2_2.addWidget(labl)
        # self.ttplValueLabel = qt.QLabel("0.00")
        # self.ttplValueLabel.setFixedWidth(short_label_width)
        # self.ttplValueLabel.setAlignment(qt.Qt.AlignLeft)
        # lout_2_2.addWidget(self.ttplValueLabel)
        # lout_2_3 = qt.QHBoxLayout()
        # lout_2.addLayout(lout_2_3)
        # labl = qt.QLabel("T htr:")
        # labl.setAlignment(qt.Qt.AlignRight)
        # labl.setMinimumWidth(long_label_width)
        # lout_2_3.addWidget(labl)
        # self.thtrValueLabel = qt.QLabel("0.00")
        # self.thtrValueLabel.setFixedWidth(short_label_width)
        # self.thtrValueLabel.setAlignment(qt.Qt.AlignLeft)
        # lout_2_3.addWidget(self.thtrValueLabel)
        # lout_2_4 = qt.QHBoxLayout()
        # lout_2.addLayout(lout_2_4)
        # labl = qt.QLabel("T htr dyn:")
        # labl.setAlignment(qt.Qt.AlignRight)
        # labl.setMinimumWidth(long_label_width)
        # lout_2_4.addWidget(labl)
        # labl.setAlignment(qt.Qt.AlignRight)
        # lout_2_4.addWidget(labl)
        # self.thtrdynValueLabel = qt.QLabel("0.00")
        # self.thtrdynValueLabel.setFixedWidth(short_label_width)
        # self.thtrdynValueLabel.setAlignment(qt.Qt.AlignLeft)
        # lout_2_4.addWidget(self.thtrdynValueLabel)
        
        # lout_2 = qt.QVBoxLayout()
        # lout_1.addLayout(lout_2)
        # lout_2_1 = qt.QHBoxLayout()
        # lout_2.addLayout(lout_2_1)
        # labl = qt.QLabel("T-error:")
        # labl.setAlignment(qt.Qt.AlignRight)
        # labl.setMinimumWidth(40)
        # lout_2_1.addWidget(labl)
        # self.terrorValueLabel = qt.QLabel("0.00")
        # self.terrorValueLabel.setFixedWidth(short_label_width)
        # self.terrorValueLabel.setAlignment(qt.Qt.AlignLeft)
        # lout_2_1.addWidget(self.terrorValueLabel)
        # lout_2_2 = qt.QVBoxLayout()
        # lout_2.addLayout(lout_2_2)
        # lout_2_2.setSpacing(1)
        # lout_2_2.setAlignment(qt.Qt.AlignCenter)
        # self.terror0Button = qt.QPushButton("> 0 <")
        # self.terror0Button.setFixedWidth(short_button_width)
        # lout_2_2.addWidget(self.terror0Button)
        # self.tresetButton = qt.QPushButton("reset")
        # self.tresetButton.setFixedWidth(short_button_width)
        # lout_2_2.addWidget(self.tresetButton)
        # lout_2.addStretch()

        # lout_1.addStretch()
        # vline = qt.QFrame()
        # vline.setFrameShape(qt.QFrame.VLine)
        # vline.setStyleSheet("color: rgb(220, 220, 220);")
        # lout_1.addWidget(vline)
        # lout_1.addStretch()

        # lout_2 = qt.QVBoxLayout()
        # lout_1.addLayout(lout_2)
        # lout_2_1 = qt.QHBoxLayout()
        # lout_2.addLayout(lout_2_1)
        # labl = qt.QLabel("Frequency:")
        # labl.setAlignment(qt.Qt.AlignRight)
        # labl.setMinimumWidth(long_label_width)
        # lout_2_1.addWidget(labl)
        # self.frequencyValueLabel = qt.QLabel("0.00")
        # self.frequencyValueLabel.setFixedWidth(short_label_width)
        # self.frequencyValueLabel.setAlignment(qt.Qt.AlignLeft)
        # lout_2_1.addWidget(self.frequencyValueLabel)
        # lout_2_2 = qt.QHBoxLayout()
        # lout_2.addLayout(lout_2_2)
        # labl = qt.QLabel("Amplitude:")
        # labl.setAlignment(qt.Qt.AlignRight)
        # labl.setMinimumWidth(long_label_width)
        # lout_2_2.addWidget(labl)
        # self.amplitudeValueLabel = qt.QLabel("0.00")
        # self.amplitudeValueLabel.setFixedWidth(short_label_width)
        # self.amplitudeValueLabel.setAlignment(qt.Qt.AlignLeft)
        # lout_2_2.addWidget(self.amplitudeValueLabel)
        # lout_2_3 = qt.QHBoxLayout()
        # lout_2.addLayout(lout_2_3)
        # labl = qt.QLabel("Offset:")
        # labl.setAlignment(qt.Qt.AlignRight)
        # labl.setMinimumWidth(long_label_width)
        # lout_2_3.addWidget(labl)
        # self.offsetValueLabel = qt.QLabel("0.00")
        # self.offsetValueLabel.setFixedWidth(short_label_width)
        # self.offsetValueLabel.setAlignment(qt.Qt.AlignLeft)
        # lout_2_3.addWidget(self.offsetValueLabel)
        # lout_2_4 = qt.QHBoxLayout()
        # lout_2.addLayout(lout_2_4)
        # labl = qt.QLabel("Power:")
        # labl.setAlignment(qt.Qt.AlignRight)
        # labl.setMinimumWidth(long_label_width)
        # lout_2_4.addWidget(labl)
        # labl.setAlignment(qt.Qt.AlignRight)
        # lout_2_4.addWidget(labl)
        # self.powerValueLabel = qt.QLabel("0.00")
        # self.powerValueLabel.setFixedWidth(short_label_width)
        # self.powerValueLabel.setAlignment(qt.Qt.AlignLeft)
        # lout_2_4.addWidget(self.powerValueLabel)

        # lout_2 = qt.QVBoxLayout()
        # lout_1.addLayout(lout_2)
        # lout_2_1 = qt.QHBoxLayout()
        # lout_2.addLayout(lout_2_1)
        # labl = qt.QLabel("Phase:")
        # labl.setAlignment(qt.Qt.AlignRight)
        # labl.setMinimumWidth(40)
        # lout_2_1.addWidget(labl)
        # self.phaseValueLabel = qt.QLabel("0.00")
        # self.phaseValueLabel.setFixedWidth(short_label_width)
        # self.phaseValueLabel.setAlignment(qt.Qt.AlignLeft)
        # lout_2_1.addWidget(self.phaseValueLabel)
        # lout_2_2 = qt.QVBoxLayout()
        # lout_2.addLayout(lout_2_2)
        # lout_2_2.setSpacing(1)
        # lout_2_2.setAlignment(qt.Qt.AlignCenter)
        # self.phase0Button = qt.QPushButton("> 0 <")
        # self.phase0Button.setFixedWidth(short_button_width)
        # lout_2_2.addWidget(self.phase0Button)
        # self.phaseResetButton = qt.QPushButton("reset")
        # self.phaseResetButton.setFixedWidth(short_button_width)
        # lout_2_2.addWidget(self.phaseResetButton)
        # lout_2.addStretch()

        # lout_1.addStretch()
        # lout_1.addStretch()

        # # results tab
        # lout_0 = qt.QHBoxLayout()
        # self.resultTab.setLayout(lout_0)
        # ########################################################
        # self.plot = Plot1D()
        # lout_0.addWidget(self.plot)
        # ########################################################

        # #######################################################
        # # self.connect_button = qt.QPushButton("Connect")
        # # self.connect_button.setFixedWidth(long_button_width)
        # # self.temp_input = qt.QLineEdit("Temperature profile in format of [float, float, ...]")
        # # self.temp_input.setFixedWidth(long_button_width)
        # # self.time_input = qt.QLineEdit("Time profile in format of [float, float, ...]")
        # # self.time_input.setFixedWidth(long_button_width)
        # # self.arm_button = qt.QPushButton("Arm")
        # # self.arm_button.setFixedWidth(long_button_width)
        # # self.run_button = qt.QPushButton("Run")
        # # self.run_button.setFixedWidth(long_button_width)
        # # self.data_button = qt.QPushButton("Get data")
        # # self.data_button.setFixedWidth(long_button_width)
        # # self.plot_button = qt.QPushButton("Plot")
        # # self.plot_button.setFixedWidth(long_button_width)
        # # leftLayout.addWidget(self.connect_button)
        # # leftLayout.addWidget(self.temp_input)
        # # leftLayout.addWidget(self.time_input)
        # # leftLayout.addWidget(self.arm_button)
        # # leftLayout.addWidget(self.run_button)
        # # leftLayout.addWidget(self.data_button)
        # # leftLayout.addWidget(self.plot_button)
        # # 
        # ########################################################
        
        ####### Status bar
        ########################################        
        lout_0 = qt.QHBoxLayout()
        rightLayout.addLayout(lout_0)
        self.sys_setup_button = qt.QPushButton()
        self.sys_setup_button.setToolTip("Device settings")
        self.sys_setup_button.setIcon(icons.getQIcon('item-object'))
        lout_0.addWidget(self.sys_setup_button)
        lout_0.addWidget(qt.QLabel("Hardware:"))
        lout_0.addStretch()
        lout_0.addWidget(qt.QLabel("Status:"))
        lout_0.addStretch()
        lout_0.addWidget(qt.QLabel("Progress:"))
        self.progressBar = qt.QProgressBar()
        self.progressBar.setFixedWidth(400)
        lout_0.addWidget(self.progressBar)
        

if __name__ == "__main__":
    import sys
    app = qt.QApplication(sys.argv)
    example = mainWindowUi()
    example.show()
    sys.exit(app.exec())