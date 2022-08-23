import sys
from silx.gui import qt
from mainWindow import mainWindow
import os


if __name__ == "__main__":
    app = qt.QApplication(sys.argv)
    app.setStyle('Fusion')
    example = mainWindow()
    example.show()
    sys.exit(app.exec())