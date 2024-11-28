from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPointF
from random import randint
from PyQt6 import uic
import sys


class Painter(QMainWindow):
    CIRCLE = 0
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.painter = QPainter()
        self.flag = False
        self.figure = self.CIRCLE

    def paint(self, event):
        if self.flag:
            self.painter.begin(self)
        if self.figure == self.CIRCLE:
            radius = randint(20, 100)
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            self.painter.setBrush(QColor(r, g, b))
            self.painter.drawEllipse(QPointF(*self.coords), radius, radius)

    def run(self):
        self.pushButton.clicked.connect(self.paint)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Painter()
    window.show()
    sys.exit(app.exec())
