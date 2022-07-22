from silx.gui import qt
from settings import *
from errorWindow import *
from constants import SETTINGS_FILE_REL_PATH


class calibWindow(qt.QDialog):
    def __init__(self, parent=None):
        super(calibWindow, self).__init__(parent=parent)

        # ####### UI setup
        # ########################################
        self.setWindowTitle("Calibration info")
        self.setFixedHeight(400)
        self.setFixedWidth(400)
        self.setWindowFlag(qt.Qt.WindowContextHelpButtonHint, False)

        mainLayout = qt.QVBoxLayout()
        mainLayout.setAlignment(qt.Qt.AlignHCenter)
        self.setLayout(mainLayout)
        
        lout_1 = qt.QHBoxLayout()
        mainLayout.addLayout(lout_1)
        labl = qt.QLabel("Calibration info: ")
        labl.setMinimumWidth(75)
        lout_1.addWidget(labl)
        self.calibInfoInput = qt.QLineEdit()
        self.calibInfoInput.setFrame(False)
        self.calibInfoInput.setText(self.parent().calibration.comment)
        lout_1.addWidget(self.calibInfoInput)

        mainLayout.addStretch()
        mainLayout.addStretch()
        hline = qt.QFrame()
        hline.setFrameShape(qt.QFrame.HLine)
        hline.setStyleSheet("color: rgb(220, 220, 220);")
        mainLayout.addWidget(hline)


        lout_1 = qt.QHBoxLayout()
        mainLayout.addLayout(lout_1)
        lout_1.setSpacing(1)
        self.applyCalibButton = qt.QPushButton("Apply")
        self.applyCalibButton.setFocusPolicy(qt.Qt.NoFocus)
        lout_1.addWidget(self.applyCalibButton)
        self.loadCalibButton = qt.QPushButton("Load")
        self.loadCalibButton.setFocusPolicy(qt.Qt.NoFocus)
        lout_1.addWidget(self.loadCalibButton)
        self.saveCalibButton = qt.QPushButton("Save")
        self.saveCalibButton.setFocusPolicy(qt.Qt.NoFocus)
        lout_1.addWidget(self.saveCalibButton)
        self.resetCalibButton = qt.QPushButton("Reset")
        self.resetCalibButton.setFocusPolicy(qt.Qt.NoFocus)
        lout_1.addWidget(self.resetCalibButton)
        # ####### end of UI setup
        # ########################################

        self.resetCalibButton.clicked.connect(self.reset_calib)

    def reset_calib(self):
        self.parent().apply_default_calib()




if __name__ == "__main__":
    import sys
    app = qt.QApplication(sys.argv)
    example = calibWindow()
    example.show()
    sys.exit(app.exec())