import random
import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    pushButton: QPushButton

    def __init__(self):
        super().__init__()
        loadUi('./UI.ui', self)

        self.pushButton.clicked.connect(self.on_click)

        self.to_draw = False

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        if self.to_draw:
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(Qt.yellow)

            for i in range(random.randint(1, 5)):
                radius = random.randint(20, 100)
                window_size = self.size()
                x = random.randint(radius, window_size.width() - radius)
                y = random.randint(radius, window_size.height() - radius)
                painter.drawEllipse(x, y, radius, radius)

            painter.end()

            self.to_draw = False

    def on_click(self):
        self.to_draw = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())