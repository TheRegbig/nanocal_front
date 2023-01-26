import numpy as np
import pandas as pd
from silx.gui import qt
from silx.io import open
import h5py
from shutil import copy
import json

from calibWindow import *
from resultsDataWidget import resultsDataWidget


class procFastHeatWidget(qt.QWidget):
    def __init__(self, parent=None):
        super(procFastHeatWidget, self).__init__(parent=parent)

        # ####### UI setup
        # ########################################
        short_line_input_width = 60

        main_lout = qt.QHBoxLayout()
        self.setLayout(main_lout)
        
        left_lout = qt.QVBoxLayout()
        right_lout = qt.QVBoxLayout()
        left_lout.setSpacing(0)
        right_lout.setSpacing(0)
        main_lout.addLayout(left_lout, 0)
        main_lout.addLayout(right_lout, 1)

        ## Experiment files management table
        left_lout.addWidget(qt.QLabel("Experimental data"))
        self.expFilesTable = qt.QListWidget()
        self.expFilesTable.setFixedSize(200, 200)
        self.expFilesTable.setSelectionMode(qt.QAbstractItemView.ExtendedSelection)
        left_lout.addWidget(self.expFilesTable, 0)

        lout_0 = qt.QHBoxLayout()
        left_lout.addLayout(lout_0)
        self.averageButtonExpFilesTable = qt.QPushButton("Average")
        self.averageButtonExpFilesTable.setEnabled(False)
        self.removeButtonExpFilesTable = qt.QPushButton("-")
        self.removeButtonExpFilesTable.setFixedWidth(30)
        self.removeButtonExpFilesTable.setEnabled(False)
        self.addButtonExpFilesTable = qt.QPushButton("+")
        self.addButtonExpFilesTable.setFixedWidth(30)
        lout_0.addWidget(self.averageButtonExpFilesTable)
        lout_0.addStretch()
        lout_0.addWidget(self.removeButtonExpFilesTable)
        lout_0.addWidget(self.addButtonExpFilesTable)

        left_lout.addSpacing(10)

        ## Reference files management table
        left_lout.addWidget(qt.QLabel("Reference data"))
        self.emptyFilesTable = qt.QListWidget()
        self.emptyFilesTable.setFixedSize(200, 200)
        self.emptyFilesTable.setSelectionMode(qt.QAbstractItemView.ExtendedSelection)
        left_lout.addWidget(self.emptyFilesTable, 0)

        lout_0 = qt.QHBoxLayout()
        left_lout.addLayout(lout_0)
        self.averageButtonEmptyFilesTable = qt.QPushButton("Average")
        self.averageButtonEmptyFilesTable.setEnabled(False)
        self.removeButtonEmptyFilesTable = qt.QPushButton("-")
        self.removeButtonEmptyFilesTable.setFixedWidth(30)
        self.removeButtonEmptyFilesTable.setEnabled(False)
        self.addButtonEmptyFilesTable = qt.QPushButton("+")
        self.addButtonEmptyFilesTable.setFixedWidth(30)
        lout_0.addWidget(self.averageButtonEmptyFilesTable)
        lout_0.addStretch()
        lout_0.addWidget(self.removeButtonEmptyFilesTable)
        lout_0.addWidget(self.addButtonEmptyFilesTable)

        left_lout.addStretch()

        ## Left control buttons
        lout_0 = qt.QHBoxLayout()
        left_lout.addLayout(lout_0)
        self.plotButton = qt.QPushButton("Plot")
        self.plotButton.setEnabled(False)
        self.saveResultsButton = qt.QPushButton("Save")
        self.saveResultsButton.setEnabled(False)
        lout_0.addWidget(self.saveResultsButton)
        lout_0.addWidget(self.plotButton)

        ## Graph space
        self.procFastHeatGraph = resultsDataWidget(parent=self)
        self.procFastHeatGraph.curveLegendsWidgetDock.setHidden(True)
        right_lout.addWidget(self.procFastHeatGraph, 1)
        
        ## Calibration space
        self.calibrationGroupBox = qt.QGroupBox("Calibration coefficients")
        right_lout.addWidget(self.calibrationGroupBox)
        lout_1 = qt.QHBoxLayout()
        self.calibrationGroupBox.setLayout(lout_1)
        lout_1.setSpacing(1)
        lout_0.addLayout(lout_1)
        lout_1.addWidget(qt.QLabel("R<sub>h</sub>(T) = "))
        self.rcoeff1Input = qt.QLineEdit()
        self.rcoeff1Input.setFixedWidth(short_line_input_width)
        lout_1.addWidget(self.rcoeff1Input)
        lout_1.addWidget(qt.QLabel(" + T \u2219"))
        self.rcoeff2Input = qt.QLineEdit()
        self.rcoeff2Input.setFixedWidth(short_line_input_width)
        lout_1.addWidget(self.rcoeff2Input)
        lout_1.addWidget(qt.QLabel(" + T<sup>2</sup> \u2219"))
        self.rcoeff3Input = qt.QLineEdit()
        self.rcoeff3Input.setFixedWidth(short_line_input_width)
        lout_1.addWidget(self.rcoeff3Input)
        lout_1.addStretch()
        lout_1.addSpacing(short_line_input_width)
        lout_1.addWidget(qt.QLabel("R<sub>g</sub> = "))
        self.rgRhRatioInput = qt.QLineEdit()
        self.rgRhRatioInput.setFixedWidth(short_line_input_width)
        lout_1.addWidget(self.rgRhRatioInput)
        lout_1.addWidget(qt.QLabel(" \u2219 R<sub>h</sub> "))

        ## Correction space
        lout_0 = qt.QHBoxLayout()
        right_lout.addLayout(lout_0)
        self.manualCorrectionGroupBox = qt.QGroupBox("Manual correction")
        lout_0.addWidget(self.manualCorrectionGroupBox)
        lout_0.addSpacing(10)
        self.autoCorrectionGroupBox = qt.QGroupBox("Auto correction")
        lout_0.addWidget(self.autoCorrectionGroupBox)

        ## Manual Correction space
        lout_0 = qt.QVBoxLayout()
        self.manualCorrectionGroupBox.setLayout(lout_0)
        lout_1 = qt.QHBoxLayout()
        lout_0.addLayout(lout_1)
        lout_1.addStretch()
        lout_1.addWidget(qt.QLabel('smooth factor: '))
        self.smoothInput = qt.QSpinBox()
        self.smoothInput.setMinimum(1)
        self.smoothInput.setMaximum(1000)
        self.smoothInput.setValue(10)
        self.smoothInput.setFixedWidth(short_line_input_width)
        lout_1.addWidget(self.smoothInput)
        self.displayRateButton = qt.QPushButton("Display rate")
        lout_1.addWidget(self.displayRateButton)
        lout_1 = qt.QHBoxLayout()
        lout_0.addLayout(lout_1)
        lout_1.addStretch()
        lout_2 = qt.QVBoxLayout()
        lout_2.setSpacing(0)
        lout_1.addLayout(lout_2)
        lout_3 = qt.QHBoxLayout()
        lout_2.addLayout(lout_3)
        lout_3.addWidget(qt.QLabel("iso begin: "))
        self.isoBeginInput = qt.QSpinBox()
        self.isoBeginInput.setMinimum(0)
        self.isoBeginInput.setMaximum(1000000000)
        self.isoBeginInput.setValue(0)
        self.isoBeginInput.setFixedWidth(short_line_input_width)
        lout_3.addWidget(self.isoBeginInput)
        lout_3 = qt.QHBoxLayout()
        lout_2.addLayout(lout_3)
        lout_3.addWidget(qt.QLabel("iso end: "))
        self.isoEndInput = qt.QSpinBox()
        self.isoEndInput.setMinimum(0)
        self.isoEndInput.setMaximum(1000000000)
        self.isoEndInput.setValue(0)
        self.isoEndInput.setFixedWidth(short_line_input_width)
        lout_3.addWidget(self.isoEndInput)
        self.isoAutoFindButton = qt.QPushButton("Auto find")
        lout_1.addWidget(self.isoAutoFindButton)
        lout_1 = qt.QHBoxLayout()
        lout_1.setSpacing(1)
        lout_0.addLayout(lout_1)
        self.calculateManualButton = qt.QPushButton("Calculate")
        lout_1.addStretch()
        lout_1.addWidget(self.calculateManualButton)
        
        ## Auto Correction space
        lout_0 = qt.QVBoxLayout()
        self.autoCorrectionGroupBox.setLayout(lout_0)
        lout_1 = qt.QHBoxLayout()
        lout_0.addLayout(lout_1)
        lout_1.addStretch()
        self.autoOption1Selector = qt.QComboBox()
        self.autoOption1Selector.addItem("all experiment files with one reference file")
        self.autoOption1Selector.addItem("each experiment file with own reference file")
        lout_1.addWidget(self.autoOption1Selector)
        lout_1 = qt.QHBoxLayout()
        lout_0.addLayout(lout_1)
        lout_1.addStretch()
        self.autoOption2Selector = qt.QComboBox()
        self.autoOption2Selector.addItem("heat exchange auto calculation")
        self.autoOption2Selector.addItem("heat exchange constant value")
        lout_1.addWidget(self.autoOption2Selector)
        lout_1 = qt.QHBoxLayout()
        lout_0.addLayout(lout_1)
        lout_1.addStretch()
        self.calculateAutoButton = qt.QPushButton("Calculate")
        lout_1.addWidget(self.calculateAutoButton)
        self.autoCorrectionGroupBox.setEnabled(False)


        main_lout.addStretch()

        float_validator = qt.QRegExpValidator(qt.QRegExp("^[-]{0,1}[0-9]{1,5}\.[0-9]{1,10}$|^[-]{0,1}[0-9]{1,5}\.[0-9]{1,10}e[-]{0,1}[+]{0,1}[0-9]{0,2}$"))
        for item in self.findChildren(qt.QLineEdit):
            item.setAlignment(qt.Qt.AlignCenter)
            item.setCursorPosition(0)
            item.setValidator(float_validator)

        ## Signals and slots
        self.addButtonExpFilesTable.clicked.connect(self.addFilesToTable)
        self.expFilesTable.itemSelectionChanged.connect(lambda: self.removeButtonExpFilesTable.setEnabled(True))
        self.expFilesTable.itemSelectionChanged.connect(lambda: self.removeButtonExpFilesTable.setEnabled(False)
                                                                    if (len(self.expFilesTable.selectedIndexes())==0) else None)
        self.expFilesTable.itemSelectionChanged.connect(lambda: self.averageButtonExpFilesTable.setEnabled(True))
        self.removeButtonExpFilesTable.clicked.connect(self.removeFilesFromTable)
        self.averageButtonExpFilesTable.clicked.connect(self.averageDataSelector)
        self.expFilesTable.itemSelectionChanged.connect(lambda: self.averageButtonExpFilesTable.setEnabled(True))
        self.expFilesTable.itemSelectionChanged.connect(lambda: self.averageButtonExpFilesTable.setEnabled(False)
                                                                    if (len(self.expFilesTable.selectedIndexes())==0) else None)

        self.addButtonEmptyFilesTable.clicked.connect(self.addFilesToTable)
        self.emptyFilesTable.itemSelectionChanged.connect(lambda: self.removeButtonEmptyFilesTable.setEnabled(True))
        self.emptyFilesTable.itemSelectionChanged.connect(lambda: self.removeButtonEmptyFilesTable.setEnabled(False)
                                                                    if (len(self.emptyFilesTable.selectedIndexes())==0) else None)
        self.emptyFilesTable.itemSelectionChanged.connect(lambda: self.averageButtonEmptyFilesTable.setEnabled(True))
        self.removeButtonEmptyFilesTable.clicked.connect(self.removeFilesFromTable)
        self.averageButtonEmptyFilesTable.clicked.connect(self.averageDataSelector)
        self.emptyFilesTable.itemSelectionChanged.connect(lambda: self.averageButtonEmptyFilesTable.setEnabled(True))
        self.emptyFilesTable.itemSelectionChanged.connect(lambda: self.averageButtonEmptyFilesTable.setEnabled(False)
                                                                    if (len(self.emptyFilesTable.selectedIndexes())==0) else None)


        self.tablesStateInstance = tablesState(mainWindow=self)
        self.tablesStateInstance.state.connect(self.autoCorrectionGroupBox.setEnabled)
        self.tablesStateInstance.state.connect(self.manualCorrectionGroupBox.setEnabled)
        self.tablesStateInstance.state.connect(self.calibrationGroupBox.setEnabled)
        self.updateButtonStates()


    def addFilesToTable(self):
        # TODO: bad structure, think how to change
        # add file check - if it contains proper nanocal fast heat data 
        sender = self.sender()
        if sender == self.addButtonExpFilesTable:
            fnames = qt.QFileDialog().getOpenFileNames(self, "Select files", None, "*.h5")[0]
            exp_paths = [self.expFilesTable.item(x).text() for x in range(self.expFilesTable.count())]
            for fname in fnames:
                if fname not in exp_paths:
                    self.expFilesTable.addItem(fname)
                    self.expFilesTable.clearSelection()
        if sender == self.addButtonEmptyFilesTable:
            fnames = qt.QFileDialog().getOpenFileNames(self, "Select files", None, "*.h5")[0]
            empty_paths = [self.emptyFilesTable.item(x).text() for x in range(self.emptyFilesTable.count())]
            for fname in fnames:
                if fname not in empty_paths:
                    self.emptyFilesTable.addItem(fname)
                    self.emptyFilesTable.clearSelection()
        
        self.updatePlotAfterAddRemove()
        self.updateCalibFieldsAfterAddRemove()
        self.updateButtonStates()
        # self.clearDummy()
        
    def removeFilesFromTable(self):
        # TODO: bad structure, think how to change
        sender = self.sender()
        if sender == self.removeButtonExpFilesTable:
            index_list = sorted(self.expFilesTable.selectedIndexes(), reverse=True)
            for selection in index_list:
                fname = self.expFilesTable.item(selection.row()).text()
                self.expFilesTable.model().removeRow(selection.row())
                self.expFilesTable.clearSelection()
        if sender == self.removeButtonEmptyFilesTable:
            index_list = sorted(self.emptyFilesTable.selectedIndexes(), reverse=True)
            for selection in index_list:
                fname = self.emptyFilesTable.item(selection.row()).text()
                self.emptyFilesTable.model().removeRow(selection.row())
                self.emptyFilesTable.clearSelection()
        
        sender.setEnabled(False)
        self.updatePlotAfterAddRemove()
        self.updateCalibFieldsAfterAddRemove()
        self.updateButtonStates()
        # self.clearDummy()

    def averageDataSelector(self):
        # TODO: bad structure, think how to change
        sender = self.sender()
                                                
        if sender == self.averageButtonExpFilesTable:
            source_fnames = [self.expFilesTable.item(x.row()).text() for x in list(self.expFilesTable.selectedIndexes())]
            exp_paths = [self.expFilesTable.item(x).text() for x in range(self.expFilesTable.count())]
            avg_fname = self.getAverageDataFname(datatype='data')
            if avg_fname: 
                self.averageData(source_fnames, avg_fname)
            if avg_fname not in exp_paths:
                self.expFilesTable.addItem(avg_fname)
            self.expFilesTable.clearSelection()



        if sender == self.averageButtonEmptyFilesTable:
            source_fnames = [self.emptyFilesTable.item(x.row()).text() for x in list(self.emptyFilesTable.selectedIndexes())]
            exp_paths = [self.emptyFilesTable.item(x).text() for x in range(self.emptyFilesTable.count())]
            avg_fname = self.getAverageDataFname(datatype='data')
            if avg_fname: 
                self.averageData(source_fnames, avg_fname)
            if avg_fname not in exp_paths:
                self.emptyFilesTable.addItem(avg_fname)
            self.emptyFilesTable.clearSelection()

        # if sender == self.showRateButton:
        #     table.clearSelection()


        sender.setEnabled(False)
        self.updatePlotAfterAddRemove()
        self.updateCalibFieldsAfterAddRemove()
        self.updateButtonStates()

    def getAverageDataFname(self, datatype:str):               
        fname = qt.QFileDialog().getSaveFileName(self, "Save average "+datatype+" as...", 
                                        "./averaged_"+datatype+".h5", 
                                        "*h5 files (*.h5)")[0]
        return fname

    def averageData(self, source_fnames:list, dest_fname:str):  
        # TODO: add to check if files have the same length
        
        # copying the first file with calibration, settings and data
        # the data from other files will be averaged with data from this file
        if dest_fname!=source_fnames[0]:
            copy(source_fnames[0], dest_fname)

        for fname in source_fnames:
            with h5py.File(dest_fname, 'r+') as dest_file, h5py.File(fname, 'r') as file:
                dest_data = dest_file['data']
                data = file['data']
                for key in dest_data:
                    dest_data_column = np.array(dest_data[key][:])
                    data_column = np.array(data[key][:])
                    avg_column = np.average(np.vstack((dest_data_column, data_column)), axis=0)
                    dest_file['data'][key][:] = avg_column

        # with h5py.File(source_fnames[0], 'r') as file:
        #     calibration = file['calibration'][()].decode()
        #     settings = file['settings'][()].decode()
        # data = open(source_fnames[0]+"::/data")
        # with h5py.File(dest_fname, 'w') as file:
        #     file.create_dataset('calibration', data=calibration)
        #     file.create_dataset('settings', data=settings)
        #     data_fgroup = file.create_group('data')
        #     for key in data:
        #         data_fgroup.create_dataset(key, data=data[key][:])
        
    def updatePlotAfterAddRemove(self):
        self.procFastHeatGraph.resultPlot.clear()
        empty_paths = [self.emptyFilesTable.item(x).text() for x in range(self.emptyFilesTable.count())]
        for path in empty_paths:
            data = open(path+"::/data")
            self.procFastHeatGraph.resultPlot.addCurve(data['time'], data['temp'], 
                                                        legend=path.split('/')[-1].split('.')[0],
                                                        color = self.procFastHeatGraph.curveColors['gray'])
            data.close()
        exp_paths = [self.expFilesTable.item(x).text() for x in range(self.expFilesTable.count())]
        for path in exp_paths:
            data = open(path+"::/data")
            self.procFastHeatGraph.resultPlot.addCurve(data['time'], data['temp'], 
                                                        legend=path.split('/')[-1].split('.')[0],
                                                        color = self.procFastHeatGraph.curveColors['red'])
            data.close()
    
    def updateCalibFieldsAfterAddRemove(self):
        exp_paths = [self.expFilesTable.item(x).text() for x in range(self.expFilesTable.count())]
        if exp_paths:
            calibration_ds = open(exp_paths[0]+"::/calibration")
            self.calibration = json.loads(calibration_ds[()].decode())
            self.rcoeff1Input.setText(str(self.calibration['thtrd0']))
            self.rcoeff2Input.setText(str(self.calibration['thtrd1']))
            self.rcoeff3Input.setText(str(self.calibration['thtrd2']))
            rgRhRatio = round(self.calibration['rghtr']/self.calibration['rhtr'], 3)
            self.rgRhRatioInput.setText(str(rgRhRatio))
            calibration_ds.close()
        else:
            pass

        

    def updateButtonStates(self):
        self.tablesStateInstance.start()

# class to check if there is something in tables, to activate some ui items
class tablesState(qt.QThread):
    state = qt.pyqtSignal(bool)
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow = mainWindow
    def run(self):
        if self.mainWindow.expFilesTable.count()>0 and self.mainWindow.emptyFilesTable.count()>0:
            self.state.emit(True)
        else:
            self.state.emit(False)


if __name__ == "__main__":
    import sys
    app = qt.QApplication(sys.argv)
    app.setStyle('Fusion')
    example = procFastHeatWidget()
    example.show()
    sys.exit(app.exec())