import sys
from silx.gui import qt
from mainWindow import mainWindow


if __name__ == "__main__":
    app = qt.QApplication(sys.argv)
    example = mainWindow()
    example.show()
    sys.exit(app.exec())