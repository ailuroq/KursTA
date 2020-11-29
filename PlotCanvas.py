from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_template import FigureCanvas
import matplotlib.pyplot as plt


class PlotCanvas(FigureCanvas):
    matrix = None
    graph = None
    booleanGraph = None

    def __init__(self):
        figure = plt.figure()
        FigureCanvas.__init__(self, figure)
        self.setParent(None)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
