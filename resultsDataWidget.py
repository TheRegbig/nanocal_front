from silx.gui import qt
from silx.gui.plot import PlotWindow
from settings import *
from errorWindow import *

class resultsDataWidget(qt.QWidget):
    def __init__(self, parent=None):
        super(resultsDataWidget, self).__init__(parent=parent)

        main_lout = qt.QHBoxLayout()
        self.setLayout(main_lout)
        
        self.resultPlot = PlotWindow(logScale=False, mask=False, 
                                    roi=False, resetzoom=True,
                                    colormap=False, aspectRatio=False, 
                                    fit=True, curveStyle=False,
                                    control=True, position=True)
        self.resultPlot.show()
        main_lout.addWidget(self.resultPlot)


    def addCurve(self, x, y, legend):
        self.resultPlot.addCurve(x=x,y=y, legend=legend)
