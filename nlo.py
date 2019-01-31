import sys
import random
import os
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtCore import Qt, QObject, QEvent
from PyQt5.QtGui import QPixmap

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.nlo = bundle_dir + '\\nlo.png'
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Управление НЛО')
        self.setMouseTracking(True)
        self.pixmap = QPixmap(self.nlo)
        self.lbl = QLabel(self)
        self.lbl.setPixmap(self.pixmap)
        self.lbl2 = QLabel(self)
        self.lbl2.setPixmap(self.pixmap)
        self.lbl2.hide()
        self.xsize = self.lbl.pixmap().size().width()
        self.ysize = self.lbl.pixmap().size().height()
        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.lbl.move(self.lbl.x() - 10, self.lbl.y())
            self.lbl2.move(self.lbl2.x() - 10, self.lbl2.y())
            if self.lbl.x() <= - self.xsize:
                self.lbl.move(500 + self.lbl.x(), self.lbl.y())
                self.lbl2.hide()
            elif self.lbl2.x() > 500 - self.xsize or self.lbl.x() < 0:
                self.lbl2.move(500 + self.lbl.x(), self.lbl.y())
                self.lbl2.show()
        if event.key() == Qt.Key_Right:
            self.lbl.move(self.lbl.x() + 10, self.lbl.y())
            self.lbl2.move(self.lbl2.x() + 10, self.lbl2.y())
            if self.lbl.x() >= 500:
                self.lbl.move(0, self.lbl.y())
                self.lbl2.hide()
            elif self.lbl.x() > 500 - self.xsize or self.lbl2.x() < 0:
                self.lbl2.move(self.lbl.x() - 500, self.lbl.y())
                self.lbl2.show()
        if event.key() == Qt.Key_Up:
            self.lbl.move(self.lbl.x(), self.lbl.y() - 10)
            self.lbl2.move(self.lbl2.x(), self.lbl2.y() - 10)
            if self.lbl.y() <= - self.ysize:
                self.lbl.move(self.lbl.x(), 500 + self.lbl.y())
                self.lbl2.hide()
            elif self.lbl.y() < 0:
                self.lbl2.move(self.lbl2.x(), 500 + self.lbl.y())
                self.lbl2.show()
        if event.key() == Qt.Key_Down:
            self.lbl.move(self.lbl.x(), self.lbl.y() + 10)
            self.lbl2.move(self.lbl2.x(), self.lbl2.y() + 10)
            if self.lbl.y() >= 500:
                self.lbl.move(self.lbl2.x(), 0)
                self.lbl2.hide()
            if self.lbl.y() > 500 - self.ysize:
                self.lbl2.move(self.lbl.x(), self.lbl.y() - 500)
                self.lbl2.show()


if __name__ == '__main__':
    if getattr(sys, 'frozen', False):
        # we are running in a bundle
        frozen = 'ever so'
        bundle_dir = sys._MEIPASS
    else:
        # we are running in a normal Python environment
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
