from silx.gui import qt
from silx.gui.plot import PlotWindow, LegendSelector
from silx.gui.plot.tools.CurveLegendsWidget import CurveLegendsWidget
from silx.gui.widgets.BoxLayoutDockWidget import BoxLayoutDockWidget

from errorWindow import *
from settings import *
import functools

class resultsDataWidget(qt.QWidget):
    def __init__(self, parent=None):
        super(resultsDataWidget, self).__init__(parent=parent)

        self.curveColors = {"black":"#292828",
                            "blue":"#2544D2", 
                            "green":"#46D225", 
                            "red":"#D22525", 
                            "violet":"#9F25D2", 
                            "orange":"#D26125", 
                            "lightblue":"#25A7D2", 
                            "yellow":"#D2B325", 
                            "gray":"#5D5D5D"
                            }

        main_lout = qt.QHBoxLayout()
        self.setLayout(main_lout)
        
        self.resultPlot = PlotWindow(logScale=False, mask=False, 
                                    roi=False, resetzoom=True,
                                    colormap=False, aspectRatio=False, 
                                    fit=True, curveStyle=True,
                                    control=False, position=True)
        self.resultPlot.setGraphGrid('major')
        self.resultPlot.setAxesMargins(left=0.1, top=0.01, right=0.01, bottom=0.1)
        self.resultPlot.setDataMargins(xMinMargin=0.05, xMaxMargin=0.05, yMinMargin=0.05, yMaxMargin=0.05)
        self.resultPlot.getXAxis().setLimits(5,95)
        self.resultPlot.getYAxis().setLimits(5,95)
        
        self.resultPlot.show()
        main_lout.addWidget(self.resultPlot)

        
        self.curveLegendsWidget = CustomCurveLegendsWidget()
        self.curveLegendsWidget.setPlotWidget(self.resultPlot)
        self.curveLegendsWidgetDock = BoxLayoutDockWidget()
        self.curveLegendsWidgetDock.setWidget(self.curveLegendsWidget)
        self.curveLegendsWidgetDock.setTitleBarWidget(qt.QWidget())
        self.curveLegendsWidgetDock.setFixedHeight(30)
        self.resultPlot.addDockWidget(qt.Qt.TopDockWidgetArea, self.curveLegendsWidgetDock)

class CustomCurveLegendsWidget(CurveLegendsWidget):
    # Extension of CurveLegendWidget

    def __init__(self, parent=None):
        super(CustomCurveLegendsWidget, self).__init__(parent)

        # Activate/Deactivate curve with left click on the legend widget
        self.sigCurveClicked.connect(self._switchCurveActive)

        # Add a custom context menu
        self.setContextMenuPolicy(qt.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self._contextMenu)

    def _switchCurveActive(self, curve):
        # Set a curve as active.
        plot = curve.getPlot()
        plot.setActiveCurve(
            curve.getName() if curve != plot.getActiveCurve() else None)

    def _switchCurveVisibility(self, curve):
        # Toggle the visibility of a curve
        curve.setVisible(not curve.isVisible())
        plot = curve.getPlot()
        plot.resetZoom()

    def _switchCurveYAxis(self, curve):
        # Change the Y axis a curve is attached to.
        yaxis = curve.getYAxis()
        curve.setYAxis('left' if yaxis == 'right' else 'right')

    def _contextMenu(self, pos):
        # Create a show the context menu.

        curve = self.curveAt(pos)  # Retrieve curve from hovered legend
        if curve is not None:
            menu = qt.QMenu()  # Create the menu

            # Add an action to activate the curve
            activeCurve = curve.getPlot().getActiveCurve()
            menu.addAction('Unselect' if curve == activeCurve else 'Select',
                           functools.partial(self._switchCurveActive, curve))

            # Add an action to switch the Y axis of a curve
            yaxis = 'right' if curve.getYAxis() == 'left' else 'left'
            menu.addAction('Map to %s' % yaxis,
                           functools.partial(self._switchCurveYAxis, curve))

            # Add an action to show/hide the curve
            menu.addAction('Hide' if curve.isVisible() else 'Show',
                           functools.partial(self._switchCurveVisibility, curve))

            globalPosition = self.mapToGlobal(pos)
            menu.exec(globalPosition)
    
if __name__ == "__main__":
    import sys
    app = qt.QApplication(sys.argv)
    app.setStyle('Fusion')
    example = resultsDataWidget()
    example.resultPlot.addCurve([0,1], [0,1], legend="first")
    example.resultPlot.addCurve([0,2], [0,1], legend="second")
    example.show()
    sys.exit(app.exec())