from silx.gui import qt
from silx.gui.plot import Plot1D, PlotWindow
from silx.gui import icons
from resultsDataWidget import resultsDataWidget

class mainWindowUi(qt.QWidget):
    def __init__(self, parent=None):
        super(mainWindowUi, self).__init__(parent)
        self.setWindowTitle("Nanocontol")
        self.setMinimumHeight(800)

        mainLayout = qt.QHBoxLayout()
        self.setLayout(mainLayout)

        short_label_width = 55
        short_button_width = 60
        long_label_width = 60
        button_height = 20
        short_line_input_width = 60
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
        self.sysOnButton = qt.QPushButton(" ON ")
        font.setBold(True)
        self.sysOnButton.setFont(font)
        self.sysOnButton.setMinimumHeight(23)
        lout_1.addWidget(self.sysOnButton, 1)
        self.sysOffButton = qt.QPushButton("OFF")
        font.setBold(True)
        self.sysOffButton.setFont(font)
        self.sysOffButton.setMinimumHeight(23)
        lout_1.addWidget(self.sysOffButton, 1)
        self.sysSetupButton = qt.QToolButton()
        self.sysSetupButton.setToolTip("Device settings")
        self.sysSetupButton.setIcon(icons.getQIcon('item-object'))
        lout_1.addWidget(self.sysSetupButton, 0)
        lout_1.setSpacing(1)

        self.sysNoHardware = qt.QCheckBox(" run without hardware")
        lout_0.addWidget(self.sysNoHardware)

        
        # ####### Experiment Group Box
        # ########################################
        self.experimentBox = qt.QGroupBox("Experiment")
        leftLayout.addWidget(self.experimentBox, 0)
        lout_0 = qt.QVBoxLayout()
        self.experimentBox.setLayout(lout_0)

        lout_0.addStretch()
        hline = qt.QFrame()
        hline.setFrameShape(qt.QFrame.HLine)
        hline.setStyleSheet("color: rgb(220, 220, 220);")
        lout_0.addWidget(hline)
        lout_0.addStretch()

        lout_1 = qt.QVBoxLayout()
        lout_0.addLayout(lout_1)
        lout_1.setSpacing(1)
        lout_1.addWidget(qt.QLabel("Data path"))
        lout_2 = qt.QHBoxLayout()
        lout_2.setSpacing(0)
        lout_1.addLayout(lout_2)
        self.sysDataPathInput = qt.QLineEdit()
        self.sysDataPathInput.setMinimumWidth(150)
        self.sysDataPathInput.setFrame(False)
        lout_2.addWidget(self.sysDataPathInput)
        self.sysDataPathButton = qt.QToolButton()
        self.sysDataPathButton.setToolTip("Browse data path")
        self.sysDataPathButton.setIcon(icons.getQIcon('document-open'))
        lout_2.addWidget(self.sysDataPathButton)

        lout_1 = qt.QVBoxLayout()
        lout_0.addLayout(lout_1)
        lout_1.setSpacing(3)
        lout_1.addWidget(qt.QLabel("Calibration path"))
        lout_2 = qt.QHBoxLayout()
        lout_1.addLayout(lout_2)
        lout_2.setSpacing(0)
        self.calibPathInput = qt.QLineEdit()
        self.calibPathInput.setFrame(False)
        lout_2.addWidget(self.calibPathInput)
        self.calibPathButton = qt.QToolButton()
        self.calibPathButton.setToolTip("Browse calibration path")
        self.calibPathButton.setIcon(icons.getQIcon('document-open'))
        lout_2.addWidget(self.calibPathButton)
        lout_3 = qt.QHBoxLayout()
        lout_3.setSpacing(1)
        lout_1.addLayout(lout_3)
        lout_3.addStretch()
        self.calibViewButton = qt.QPushButton("View")
        self.calibViewButton.setFixedWidth(short_button_width)
        lout_3.addWidget(self.calibViewButton)
        self.calibApplyButton = qt.QPushButton("Apply")
        self.calibApplyButton.setFixedWidth(short_button_width)
        lout_3.addWidget(self.calibApplyButton)

        lout_0.addStretch()
        hline = qt.QFrame()
        hline.setFrameShape(qt.QFrame.HLine)
        hline.setStyleSheet("color: rgb(220, 220, 220);")
        lout_0.addWidget(hline)
        lout_0.addStretch()

        lout_1 = qt.QVBoxLayout()
        lout_0.addLayout(lout_1)
        lout_1.setSpacing(3)
        lout_1.addWidget(qt.QLabel("Scan"))
        lout_2 = qt.QHBoxLayout()
        lout_1.addLayout(lout_2)
        lout_2.setSpacing(3)
        lout_2.addStretch()
        lout_2.addWidget(qt.QLabel("Sample rate:"))
        self.scanSampleRateInput = qt.QLineEdit()
        self.scanSampleRateInput.setMaximumWidth(short_line_input_width)
        self.scanSampleRateInput.setFrame(False)
        lout_2.addWidget(self.scanSampleRateInput)
        unit = qt.QLabel("Hz")
        unit.setFixedWidth(20)
        lout_2.addWidget(unit)
        lout_3 = qt.QHBoxLayout()
        lout_1.addLayout(lout_3)
        lout_3.setSpacing(1)
        lout_3.addStretch()
        self.resetScanSampleRateButton = qt.QPushButton("Reset")
        self.resetScanSampleRateButton.setFixedWidth(short_button_width)
        lout_3.addWidget(self.resetScanSampleRateButton)
        self.applyScanSampleRateButton = qt.QPushButton("Apply")
        self.applyScanSampleRateButton.setFixedWidth(short_button_width)
        lout_3.addWidget(self.applyScanSampleRateButton)

        lout_0.addStretch()
        hline = qt.QFrame()
        hline.setFrameShape(qt.QFrame.HLine)
        hline.setStyleSheet("color: rgb(220, 220, 220);")
        lout_0.addWidget(hline)
        lout_0.addStretch()

        lout_1 = qt.QVBoxLayout()
        lout_0.addLayout(lout_1)
        lout_1.setSpacing(3)
        lout_1.addWidget(qt.QLabel("Modulation"))
        lout_2 = qt.QHBoxLayout()
        lout_1.addLayout(lout_2)
        lout_2.setSpacing(3)
        lout_2.addStretch()
        lout_2.addWidget(qt.QLabel("Frequency:"))
        self.freqInput = qt.QLineEdit()
        self.freqInput.setMaximumWidth(short_line_input_width)
        self.freqInput.setFrame(False)
        lout_2.addWidget(self.freqInput)
        units = qt.QLabel("Hz")
        units.setFixedWidth(20)
        lout_2.addWidget(units)
        lout_3 = qt.QHBoxLayout()
        lout_1.addLayout(lout_3)
        lout_3.setSpacing(3)
        lout_3.addStretch()
        lout_3.addWidget(qt.QLabel("Amplitude:"))
        self.amplitudeInput = qt.QLineEdit()
        self.amplitudeInput.setMaximumWidth(short_line_input_width)
        self.amplitudeInput.setFrame(False)
        lout_3.addWidget(self.amplitudeInput)
        units = qt.QLabel("mA")
        units.setFixedWidth(20)
        lout_3.addWidget(units)
        lout_4 = qt.QHBoxLayout()
        lout_1.addLayout(lout_4)
        lout_4.setSpacing(3)
        lout_4.addStretch()
        lout_4.addWidget(qt.QLabel("Offset:"))
        self.offsetInput = qt.QLineEdit()
        self.offsetInput.setMaximumWidth(short_line_input_width)
        self.offsetInput.setFrame(False)
        lout_4.addWidget(self.offsetInput)
        units = qt.QLabel("mA")
        units.setFixedWidth(20)
        lout_4.addWidget(units)
        lout_5 = qt.QHBoxLayout()
        lout_1.addLayout(lout_5)
        lout_5.setSpacing(1)
        lout_5.addStretch()
        self.resetModulationParamsButton = qt.QPushButton("Reset")
        self.resetModulationParamsButton.setFixedWidth(short_button_width)
        lout_5.addWidget(self.resetModulationParamsButton)
        self.applyModulationParamsButton = qt.QPushButton("Apply")
        self.applyModulationParamsButton.setFixedWidth(short_button_width)
        lout_5.addWidget(self.applyModulationParamsButton)

        # lout_0.addStretch()

        leftLayout.addStretch(2)

        # ####### Logo
        # ########################################
        lout_0 = qt.QVBoxLayout()
        leftLayout.addLayout(lout_0, 0)
        logo = qt.QLabel()
        logo.setAlignment(qt.Qt.AlignHCenter)
        pixmap = qt.QPixmap("./res/logo.png").scaledToWidth(70)
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
        
        # Control tab
        lout_0 = qt.QVBoxLayout()
        self.controlTab.setLayout(lout_0)
        lout_1 = qt.QHBoxLayout()
        lout_0.addLayout(lout_1, 1)
        
        # Prog group box
        self.progGroupBox = qt.QGroupBox("Prog")
        lout_1.addWidget(self.progGroupBox, 0)
        lout_2 = qt.QVBoxLayout()
        lout_2.setSpacing(0)
        self.progGroupBox.setLayout(lout_2)
        
        lout_3 = qt.QHBoxLayout()
        lout_3.setSpacing(0)
        lout_2.addLayout(lout_3)
        self.experimentTimeComboBox = qt.QComboBox()
        self.experimentTimeComboBox.setFixedWidth(75)
        self.experimentTimeComboBox.addItem("Time (ms)")
        self.experimentTimeComboBox.addItem("Time (s)")
        lout_3.addWidget(self.experimentTimeComboBox)
        self.experimentTempComboBox = qt.QComboBox()
        self.experimentTempComboBox.setFixedWidth(75)
        self.experimentTempComboBox.addItem("Temp (°C)")
        self.experimentTempComboBox.addItem("Volt (V)")
        lout_3.addWidget(self.experimentTempComboBox)

        lout_3 = qt.QHBoxLayout()
        lout_3.setSpacing(0)
        lout_2.addLayout(lout_3)
        self.experimentTable = qt.QTableWidget()
        self.experimentTable.setFixedSize(150, 207)
        self.experimentTable.setFrameStyle(qt.QFrame.NoFrame)
        # self.experimentTable.setFrameStyle(qt.QFrame.StyledPanel)
        self.experimentTable.setRowCount(100)
        self.experimentTable.setColumnCount(2)
        self.experimentTable.horizontalHeader().setVisible(False)
        self.experimentTable.horizontalHeader().setDefaultSectionSize(75)
        self.experimentTable.horizontalHeader().setHighlightSections(False)
        self.experimentTable.horizontalHeader().setMinimumSectionSize(75)
        self.experimentTable.verticalHeader().setVisible(False)
        self.experimentTable.verticalHeader().setDefaultSectionSize(10)
        self.experimentTable.verticalHeader().setMinimumSectionSize(10)
        self.experimentTable.setVerticalScrollBarPolicy(qt.Qt.ScrollBarAlwaysOff)
        self.experimentTable.setHorizontalScrollBarPolicy(qt.Qt.ScrollBarAlwaysOff)
        self.experimentTable.setColumnWidth(0,75)
        self.experimentTable.setColumnWidth(1,75)
        self.experimentTable.setInputMethodHints(qt.Qt.ImhNone)
        for row in range(100):
            for col in range(2):
                item = qt.QTableWidgetItem('0')
                item.setTextAlignment(qt.Qt.AlignCenter)
                self.experimentTable.setItem(row, col, item)
        self.experimentTable.setFocusPolicy(qt.Qt.NoFocus)
        palette = self.experimentTable.palette()
        palette.setColor(qt.QPalette.Inactive, qt.QPalette.Highlight, qt.Qt.transparent)
        self.experimentTable.setPalette(palette)
        self.experimentTable.setEditTriggers(qt.QAbstractItemView.AllEditTriggers)
        self.experimentTable.resizeRowsToContents()
        lout_3.addWidget(self.experimentTable, 0)

        lout_2.addSpacing(5)

        lout_3 = qt.QHBoxLayout()
        lout_3.setSpacing(1)
        lout_2.addLayout(lout_3)
        self.loadTxtButton = qt.QPushButton("Load")
        lout_3.addWidget(self.loadTxtButton)
        self.armButton = qt.QPushButton("Arm")
        lout_3.addWidget(self.armButton)

        lout_2.addSpacing(5)

        lout_3 = qt.QHBoxLayout()
        lout_3.setSpacing(1)
        lout_2.addLayout(lout_3)
        self.stopButton = qt.QPushButton("Stop")
        lout_3.addWidget(self.stopButton)
        self.startButton = qt.QPushButton("Start")
        lout_3.addWidget(self.startButton)

        lout_2.addStretch()

        lout_3 = qt.QHBoxLayout()
        lout_3.setSpacing(1)
        lout_2.addLayout(lout_3)
        voltLabel = qt.QLabel("Volt (V)")
        voltLabel.setAlignment(qt.Qt.AlignCenter)
        lout_3.addWidget(voltLabel)
        tempLabel = qt.QLabel("Temp (°C)")
        tempLabel.setAlignment(qt.Qt.AlignCenter)
        lout_3.addWidget(tempLabel)
        
        lout_3 = qt.QHBoxLayout()
        lout_3.setSpacing(0)
        lout_2.addLayout(lout_3)
        self.setTable = qt.QTableWidget()
        self.setTable.setFixedSize(150, 23)
        self.setTable.setFrameStyle(qt.QFrame.NoFrame)
        # self.setTable.setFrameStyle(qt.QFrame.StyledPanel)
        self.setTable.setRowCount(1)
        self.setTable.setColumnCount(2)
        self.setTable.horizontalHeader().setVisible(False)
        self.setTable.horizontalHeader().setDefaultSectionSize(75)
        self.setTable.horizontalHeader().setHighlightSections(False)
        self.setTable.horizontalHeader().setMinimumSectionSize(75)
        self.setTable.verticalHeader().setVisible(False)
        self.setTable.verticalHeader().setDefaultSectionSize(10)
        self.setTable.verticalHeader().setMinimumSectionSize(10)
        self.setTable.setVerticalScrollBarPolicy(qt.Qt.ScrollBarAlwaysOff)
        self.setTable.setHorizontalScrollBarPolicy(qt.Qt.ScrollBarAlwaysOff)
        self.setTable.setColumnWidth(0,75)
        self.setTable.setColumnWidth(1,75)
        self.setTable.setInputMethodHints(qt.Qt.ImhNone)
        item = qt.QTableWidgetItem('0')
        item.setTextAlignment(qt.Qt.AlignCenter)
        self.setTable.setItem(0, 0, item)
        item = qt.QTableWidgetItem('0')
        item.setTextAlignment(qt.Qt.AlignCenter)
        self.setTable.setItem(0, 1, item)
        self.setTable.setFocusPolicy(qt.Qt.NoFocus)
        palette = self.setTable.palette()
        palette.setColor(qt.QPalette.Inactive, qt.QPalette.Highlight, qt.Qt.transparent)
        self.setTable.setPalette(palette)
        self.setTable.setEditTriggers(qt.QAbstractItemView.AllEditTriggers)
        self.setTable.resizeRowsToContents()
        lout_3.addWidget(self.setTable, 0)
        lout_2.addSpacing(5)
        lout_3 = qt.QHBoxLayout()
        lout_3.setSpacing(1)
        lout_2.addLayout(lout_3)
        self.offTempVoltButton = qt.QPushButton("Stop")
        lout_3.addWidget(self.offTempVoltButton)
        self.setTempVoltButton = qt.QPushButton("Set")
        lout_3.addWidget(self.setTempVoltButton)

        # Signal and program plots 
        self.controlTabsWidget = qt.QTabWidget()
        self.signalsTab = qt.QWidget()
        self.controlTabsWidget.addTab(self.signalsTab, "Signals")
        self.progTab = qt.QWidget()
        self.controlTabsWidget.addTab(self.progTab, "Program")
        lout_1.addWidget(self.controlTabsWidget, 1)
        lout_2 = qt.QVBoxLayout()
        self.signalsTab.setLayout(lout_2)
        self.signalsPlot = PlotWindow(fit=False, mask=False, roi=False, colormap=False,
                                    curveStyle=False, yInverted=False, logScale=False,
                                    aspectRatio=False)
        self.signalsPlot.setAxesMargins(left=0.005, top=0.005, right=0.005, bottom=0.005)
        self.signalsPlot.setDataMargins(xMinMargin=0.05, xMaxMargin=0.05, yMinMargin=0.05, yMaxMargin=0.05)
        self.signalsPlot.getYAxis().setLabel('')
        self.signalsPlot.getXAxis().setLabel('')
        self.signalsPlot.setGraphGrid('major')
        self.signalsPlot.addCurve([0,1], [0,1], linestyle='') # just for better view at start
        lout_2.addWidget(self.signalsPlot)
        lout_3 = qt.QVBoxLayout()
        self.progTab.setLayout(lout_3)
        self.progPlot = PlotWindow(fit=False, mask=False, roi=False, colormap=False,
                                    curveStyle=False, yInverted=False, logScale=False,
                                    aspectRatio=False)
        self.progPlot.setAxesMargins(left=0.1, top=0.05, right=0.05, bottom=0.1)
        self.progPlot.setDataMargins(xMinMargin=0.05, xMaxMargin=0.05, yMinMargin=0.05, yMaxMargin=0.05)
        self.progPlot.getXAxis().setLabel(self.experimentTimeComboBox.currentText())
        self.progPlot.getYAxis().setLabel(self.experimentTempComboBox.currentText())
        self.progPlot.setGraphGrid('major')
        self.progPlot.addCurve([0,1], [0,1], linestyle='')
        lout_3.addWidget(self.progPlot)

        # Values area
        self.valuesBox = qt.QGroupBox("Values")
        lout_0.addWidget(self.valuesBox, 0)
        lout_1 = qt.QHBoxLayout()
        self.valuesBox.setLayout(lout_1)
        
        lout_1.addStretch()
        lout_1.addStretch()

        lout_2 = qt.QVBoxLayout()
        lout_1.addLayout(lout_2)
        lout_2_1 = qt.QHBoxLayout()
        lout_2.addLayout(lout_2_1)
        labl = qt.QLabel("R htr abs:")
        labl.setAlignment(qt.Qt.AlignRight)
        lout_2_1.addWidget(labl)
        self.rhtrabsValueLabel = qt.QLabel(" ---")
        self.rhtrabsValueLabel.setFixedWidth(short_label_width)
        self.rhtrabsValueLabel.setAlignment(qt.Qt.AlignLeft)
        lout_2_1.addWidget(self.rhtrabsValueLabel)
        lout_2_2 = qt.QHBoxLayout()
        lout_2.addLayout(lout_2_2)
        labl = qt.QLabel("R htr dyn:")
        labl.setAlignment(qt.Qt.AlignRight)
        lout_2_2.addWidget(labl)
        self.rhtrdynValueLabel = qt.QLabel(" ---")
        self.rhtrdynValueLabel.setFixedWidth(short_label_width)
        self.rhtrdynValueLabel.setAlignment(qt.Qt.AlignLeft)
        lout_2_2.addWidget(self.rhtrdynValueLabel)
        lout_2_3 = qt.QHBoxLayout()
        lout_2.addLayout(lout_2_3)
        labl = qt.QLabel("U mod htr:")
        labl.setAlignment(qt.Qt.AlignRight)
        lout_2_3.addWidget(labl)
        self.umodhtrValueLabel = qt.QLabel(" ---")
        self.umodhtrValueLabel.setFixedWidth(short_label_width)
        self.umodhtrValueLabel.setAlignment(qt.Qt.AlignLeft)
        lout_2_3.addWidget(self.umodhtrValueLabel)
        lout_2_4 = qt.QHBoxLayout()
        lout_2.addLayout(lout_2_4)
        labl = qt.QLabel("I htr:")
        labl.setAlignment(qt.Qt.AlignRight)
        lout_2_4.addWidget(labl)
        labl.setAlignment(qt.Qt.AlignRight)
        lout_2_4.addWidget(labl)
        self.ihtrValueLabel = qt.QLabel(" ---")
        self.ihtrValueLabel.setFixedWidth(short_label_width)
        self.ihtrValueLabel.setAlignment(qt.Qt.AlignLeft)
        lout_2_4.addWidget(self.ihtrValueLabel)

        lout_1.addStretch()
        vline = qt.QFrame()
        vline.setFrameShape(qt.QFrame.VLine)
        vline.setStyleSheet("color: rgb(220, 220, 220);")
        lout_1.addWidget(vline)
        lout_1.addStretch()

        lout_2 = qt.QVBoxLayout()
        lout_1.addLayout(lout_2)
        lout_2_1 = qt.QHBoxLayout()
        lout_2.addLayout(lout_2_1)
        labl = qt.QLabel("T aux:")
        labl.setAlignment(qt.Qt.AlignRight)
        lout_2_1.addWidget(labl)
        self.tauxValueLabel = qt.QLabel(" ---")
        self.tauxValueLabel.setFixedWidth(short_label_width)
        self.tauxValueLabel.setAlignment(qt.Qt.AlignLeft)
        lout_2_1.addWidget(self.tauxValueLabel)
        lout_2_2 = qt.QHBoxLayout()
        lout_2.addLayout(lout_2_2)
        labl = qt.QLabel("T tpl:")
        labl.setAlignment(qt.Qt.AlignRight)
        lout_2_2.addWidget(labl)
        self.ttplValueLabel = qt.QLabel(" ---")
        self.ttplValueLabel.setFixedWidth(short_label_width)
        self.ttplValueLabel.setAlignment(qt.Qt.AlignLeft)
        lout_2_2.addWidget(self.ttplValueLabel)
        lout_2_3 = qt.QHBoxLayout()
        lout_2.addLayout(lout_2_3)
        labl = qt.QLabel("T htr:")
        labl.setAlignment(qt.Qt.AlignRight)
        lout_2_3.addWidget(labl)
        self.thtrValueLabel = qt.QLabel(" ---")
        self.thtrValueLabel.setFixedWidth(short_label_width)
        self.thtrValueLabel.setAlignment(qt.Qt.AlignLeft)
        lout_2_3.addWidget(self.thtrValueLabel)
        lout_2_4 = qt.QHBoxLayout()
        lout_2.addLayout(lout_2_4)
        labl = qt.QLabel("T htr dyn:")
        labl.setAlignment(qt.Qt.AlignRight)
        lout_2_4.addWidget(labl)
        labl.setAlignment(qt.Qt.AlignRight)
        lout_2_4.addWidget(labl)
        self.thtrdynValueLabel = qt.QLabel(" ---")
        self.thtrdynValueLabel.setFixedWidth(short_label_width)
        self.thtrdynValueLabel.setAlignment(qt.Qt.AlignLeft)
        lout_2_4.addWidget(self.thtrdynValueLabel)
        
        lout_2 = qt.QVBoxLayout()
        lout_1.addLayout(lout_2)
        lout_2_1 = qt.QHBoxLayout()
        lout_2.addLayout(lout_2_1)
        labl = qt.QLabel("T-error:")
        labl.setAlignment(qt.Qt.AlignRight)
        lout_2_1.addWidget(labl)
        self.terrorValueLabel = qt.QLabel(" --")
        self.terrorValueLabel.setFixedWidth(30)
        self.terrorValueLabel.setAlignment(qt.Qt.AlignLeft)
        lout_2_1.addWidget(self.terrorValueLabel)
        lout_2_2 = qt.QVBoxLayout()
        lout_2.addLayout(lout_2_2)
        lout_2_2.setSpacing(1)
        lout_2_2.setAlignment(qt.Qt.AlignCenter)
        self.terror0Button = qt.QPushButton("> 0 <")
        self.terror0Button.setFixedWidth(short_button_width)
        lout_2_2.addWidget(self.terror0Button)
        self.tresetButton = qt.QPushButton("reset")
        self.tresetButton.setFixedWidth(short_button_width)
        lout_2_2.addWidget(self.tresetButton)
        lout_2.addStretch()

        lout_1.addStretch()
        vline = qt.QFrame()
        vline.setFrameShape(qt.QFrame.VLine)
        vline.setStyleSheet("color: rgb(220, 220, 220);")
        lout_1.addWidget(vline)
        lout_1.addStretch()

        lout_2 = qt.QVBoxLayout()
        lout_1.addLayout(lout_2)
        lout_2_1 = qt.QHBoxLayout()
        lout_2.addLayout(lout_2_1)
        labl = qt.QLabel("Frequency:")
        labl.setAlignment(qt.Qt.AlignRight)
        lout_2_1.addWidget(labl)
        self.frequencyValueLabel = qt.QLabel(" ---")
        self.frequencyValueLabel.setFixedWidth(short_label_width)
        self.frequencyValueLabel.setAlignment(qt.Qt.AlignLeft)
        lout_2_1.addWidget(self.frequencyValueLabel)
        lout_2_2 = qt.QHBoxLayout()
        lout_2.addLayout(lout_2_2)
        labl = qt.QLabel("Amplitude:")
        labl.setAlignment(qt.Qt.AlignRight)
        lout_2_2.addWidget(labl)
        self.amplitudeValueLabel = qt.QLabel(" ---")
        self.amplitudeValueLabel.setFixedWidth(short_label_width)
        self.amplitudeValueLabel.setAlignment(qt.Qt.AlignLeft)
        lout_2_2.addWidget(self.amplitudeValueLabel)
        lout_2_3 = qt.QHBoxLayout()
        lout_2.addLayout(lout_2_3)
        labl = qt.QLabel("Offset:")
        labl.setAlignment(qt.Qt.AlignRight)
        lout_2_3.addWidget(labl)
        self.offsetValueLabel = qt.QLabel(" ---")
        self.offsetValueLabel.setFixedWidth(short_label_width)
        self.offsetValueLabel.setAlignment(qt.Qt.AlignLeft)
        lout_2_3.addWidget(self.offsetValueLabel)
        lout_2_4 = qt.QHBoxLayout()
        lout_2.addLayout(lout_2_4)
        labl = qt.QLabel("Power:")
        labl.setAlignment(qt.Qt.AlignRight)
        lout_2_4.addWidget(labl)
        labl.setAlignment(qt.Qt.AlignRight)
        lout_2_4.addWidget(labl)
        self.powerValueLabel = qt.QLabel(" ---")
        self.powerValueLabel.setFixedWidth(short_label_width)
        self.powerValueLabel.setAlignment(qt.Qt.AlignLeft)
        lout_2_4.addWidget(self.powerValueLabel)

        lout_2 = qt.QVBoxLayout()
        lout_1.addLayout(lout_2)
        lout_2_1 = qt.QHBoxLayout()
        lout_2.addLayout(lout_2_1)
        labl = qt.QLabel("Phase:")
        labl.setAlignment(qt.Qt.AlignRight)
        lout_2_1.addWidget(labl)
        self.phaseValueLabel = qt.QLabel(" --")
        self.phaseValueLabel.setFixedWidth(30)
        self.phaseValueLabel.setAlignment(qt.Qt.AlignLeft)
        lout_2_1.addWidget(self.phaseValueLabel)
        lout_2_2 = qt.QVBoxLayout()
        lout_2.addLayout(lout_2_2)
        lout_2_2.setSpacing(1)
        lout_2_2.setAlignment(qt.Qt.AlignCenter)
        self.phase0Button = qt.QPushButton("> 0 <")
        self.phase0Button.setFixedWidth(short_button_width)
        lout_2_2.addWidget(self.phase0Button)
        self.phaseResetButton = qt.QPushButton("reset")
        self.phaseResetButton.setFixedWidth(short_button_width)
        lout_2_2.addWidget(self.phaseResetButton)
        lout_2.addStretch()

        lout_1.addStretch()
        lout_1.addStretch()

        # results tab
        lout_0 = qt.QHBoxLayout()
        self.resultTab.setLayout(lout_0)
        self.resultsDataWidget = resultsDataWidget(parent=self)
        lout_0.addWidget(self.resultsDataWidget)

        # ########################################################

        
        ####### Status bar
        ########################################        
        lout_0 = qt.QHBoxLayout()
        rightLayout.addLayout(lout_0)
        lout_0.setSpacing(1)
        lout_0.addWidget(qt.QLabel("Hardware:"))
        self.hardware_label = qt.QLabel(' ---')
        self.hardware_label.setFixedWidth(80)
        lout_0.addWidget(self.hardware_label)
        lout_0.addWidget(qt.QLabel("Status:"))
        self.status_label = qt.QLabel(' ---')
        self.status_label.setFixedWidth(80)
        lout_0.addWidget(self.status_label)
        lout_0.addStretch()
        lout_0.addWidget(qt.QLabel("Progress:"))
        self.progressBar = qt.QProgressBar()
        lout_0.addWidget(self.progressBar,1)
        
        ####### Filtering input
        #######################################
        class TableDelegate(qt.QItemDelegate):
            def __init__(self, parent):
                qt.QItemDelegate.__init__(self, parent)
            def createEditor(self, parent, option, index):
                spinbox = qt.QDoubleSpinBox(parent)
                spinbox.setMaximum(100000)
                return spinbox

        self.experimentTable.setItemDelegate(TableDelegate(self.experimentTable))
        self.experimentTable.setItemDelegate(TableDelegate(self.experimentTable))
        self.setTable.setItemDelegate(TableDelegate(self.setTable))
        self.setTable.setItemDelegate(TableDelegate(self.setTable))

        float_validator_100 = qt.QRegExpValidator(qt.QRegExp("^[0-9]{1,2}\.[0-9]{1,2}$"))
        int_validator_5 = qt.QRegExpValidator(qt.QRegExp("^[0-9]{1,5}$"))

        self.scanSampleRateInput.setValidator(int_validator_5)
        self.freqInput.setValidator(float_validator_100)
        self.amplitudeInput.setValidator(float_validator_100)
        self.offsetInput.setValidator(float_validator_100)

        ####### Set items disabled
        ####################################### 
        # [item.setEnabled(False) for item in [self.experimentBox, self.controlTab]]


if __name__ == "__main__":
    import sys
    app = qt.QApplication(sys.argv)
    example = mainWindowUi()
    example.show()
    sys.exit(app.exec())
