from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QTextEdit

from PlotCanvas import PlotCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class WidgetPlot(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)
        self.setLayout(QGridLayout())
        self.canvas = PlotCanvas()
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.pybutton = QPushButton('Задать граф', self)
        self.pybutton_2 = QPushButton('Добавить вершину', self)
        self.pybutton_3 = QPushButton('Соединить вершины', self)
        self.pybutton_4 = QPushButton('Алгоритм Дейкстры', self)
        self.pybutton_5 = QPushButton('Информация о графе', self)
        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().addWidget(self.pybutton, 0, 1, 1, 1)
        self.layout().addWidget(self.pybutton_2, 0, 2, 1, 1)
        self.layout().addWidget(self.pybutton_3, 0, 3, 1, 1)
        self.layout().addWidget(self.pybutton_4, 0, 4, 1, 1)
        self.layout().addWidget(self.pybutton_5, 0, 5, 1, 1)
        self.layout().addWidget(self.toolbar, 1, 1, 1, 5)
        self.layout().addWidget(self.canvas, 2, 1, 4, 5)
