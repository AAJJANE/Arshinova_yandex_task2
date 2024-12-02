import sys
import random
from random import randint
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QPushButton, QWidget
from ui import Ui_qwidget


class PaintCircle(QWidget, Ui_qwidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.draw_circles)
        self.circles = []


    def draw_circles(self):
        self.circles.clear()
        for i in range(randint(1, 25)):
            diameter = random.randint(20, 100)
            x = random.randint(0, self.width() - diameter)
            y = random.randint(0, self.height() - diameter)
            self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for diameter, x, y in self.circles:
            color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            painter.setBrush(color)
            painter.drawEllipse(x, y, diameter, diameter)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = PaintCircle()
    window.show()
    sys.exit(app.exec())
