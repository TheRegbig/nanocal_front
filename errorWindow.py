from silx.gui import qt

class errorWindow(qt.QMessageBox):
    def __init__(self, error_text: str, parent=None):
        super(errorWindow, self).__init__(parent)
        self.setText(error_text)
        self.setWindowTitle("Error")
        self.setIcon(qt.QMessageBox.Critical)
        self.addButton(qt.QMessageBox.Ok)
        self.exec()
