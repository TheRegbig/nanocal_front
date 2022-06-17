import sys
from silx.gui import qt
from mainWindow import mainWindow
import os


if __name__ == "__main__":
    if not os.path.exists('./data'):
        os.makedirs('./data')
    app = qt.QApplication(sys.argv)
    example = mainWindow()
    example.show()
    sys.exit(app.exec())