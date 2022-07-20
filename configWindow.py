from silx.gui import qt
import os
from settings import *
from errorWindow import *
from constants import SETTINGS_FILE_REL_PATH


class configWindow(qt.QDialog):
    def __init__(self, parent=None):
        super(configWindow, self).__init__(parent=parent)

        self.setWindowTitle("Configuration")
        self.setFixedHeight(400)
        self.setFixedWidth(300)
        self.setWindowFlag(qt.Qt.WindowContextHelpButtonHint, False)

        mainLayout = qt.QVBoxLayout()
        mainLayout.setAlignment(qt.Qt.AlignHCenter)
        self.setLayout(mainLayout)

        labl = qt.QLabel("Some help will be here :)")
        labl.setAlignment(qt.Qt.AlignHCenter)
        mainLayout.addWidget(labl)
        labl = qt.QLabel("Nanocontrol v.0.1")
        labl.setAlignment(qt.Qt.AlignHCenter)
        labl.setFont(qt.QFont("Times", weight=qt.QFont.Bold))
        mainLayout.addWidget(labl)
        labl = qt.QLabel("Melnikov Alexey & Komov Evgenii")
        labl.setAlignment(qt.Qt.AlignHCenter)
        mainLayout.addWidget(labl)
        labl = qt.QLabel(u"<p><a href='"'mailto:alexey.melnikov@esrf.fr'"'>alexey.melnikov@esrf.fr</a>  </p>")
        labl.setAlignment(qt.Qt.AlignHCenter)
        mainLayout.addWidget(labl)

        mainLayout.addStretch()

        lout_1 = qt.QHBoxLayout()
        mainLayout.addLayout(lout_1)
        labl = qt.QLabel("Tango host: ")
        labl.setMinimumWidth(75)
        lout_1.addWidget(labl)
        self.tangoHostInput = qt.QLineEdit()
        self.tangoHostInput.setFrame(False)
        self.tangoHostInput.setText(self.parent().settings.tango_host)
        lout_1.addWidget(self.tangoHostInput)

        lout_1 = qt.QHBoxLayout()
        mainLayout.addLayout(lout_1)
        labl = qt.QLabel("Device proxy: ")
        labl.setMinimumWidth(75)
        lout_1.addWidget(labl)
        self.deviceProxyInput = qt.QLineEdit()
        self.deviceProxyInput.setFrame(False)
        self.deviceProxyInput.setText(self.parent().settings.device_proxy)
        lout_1.addWidget(self.deviceProxyInput)

        lout_1 = qt.QHBoxLayout()
        mainLayout.addLayout(lout_1)
        labl = qt.QLabel("HTTP host: ")
        labl.setMinimumWidth(75)
        lout_1.addWidget(labl)
        self.httpHostInput = qt.QLineEdit()
        self.httpHostInput.setFrame(False)
        self.httpHostInput.setText(self.parent().settings.http_host)
        lout_1.addWidget(self.httpHostInput)

        lout_1 = qt.QHBoxLayout()
        mainLayout.addLayout(lout_1)
        lout_1.setSpacing(1)
        self.applyConfigButton = qt.QPushButton("Apply")
        lout_1.addWidget(self.applyConfigButton)
        self.loadConfigButton = qt.QPushButton("Load")
        lout_1.addWidget(self.loadConfigButton)
        self.saveConfigButton = qt.QPushButton("Save")
        lout_1.addWidget(self.saveConfigButton)
        self.resetConfigButton = qt.QPushButton("Reset")
        lout_1.addWidget(self.resetConfigButton)

        ## end of UI setup

        self.applyConfigButton.clicked.connect(self.apply_settings)
        self.saveConfigButton.clicked.connect(self.save_settings)
        self.loadConfigButton.clicked.connect(self.load_settings)
        self.resetConfigButton.clicked.connect(self.reset_settings)

    def apply_settings(self):
        self.parent().settings.tango_host = self.tangoHostInput.text()
        self.parent().settings.device_proxy = self.deviceProxyInput.text()
        self.parent().settings.http_host = self.httpHostInput.text()

    def load_settings(self):
        self.parent().load_settings(fpath=True)
        self.tangoHostInput.setText(self.parent().settings.tango_host)
        self.deviceProxyInput.setText(self.parent().settings.device_proxy)
        self.httpHostInput.setText(self.parent().settings.http_host)

    def save_settings(self):
        self.parent().save_settings(fpath=True)
    
    def reset_settings(self):
        self.parent().reset_settings()
        self.tangoHostInput.setText(self.parent().settings.tango_host)
        self.deviceProxyInput.setText(self.parent().settings.device_proxy)
        self.httpHostInput.setText(self.parent().settings.http_host)

if __name__ == "__main__":
    import sys
    app = qt.QApplication(sys.argv)
    example = configWindow()
    example.show()
    sys.exit(app.exec())