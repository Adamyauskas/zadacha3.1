import sys
from random import randint
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_Circles(object):
    def setupUi(self, Circles):
        Circles.setObjectName("Circles")
        Circles.resize(615, 502)
        self.centralwidget = QtWidgets.QWidget(Circles)
        self.centralwidget.setObjectName("centralwidget")
        self.make_circle = QtWidgets.QPushButton(self.centralwidget)
        self.make_circle.setGeometry(QtCore.QRect(270, 370, 75, 23))
        self.make_circle.setObjectName("make_circle")
        Circles.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Circles)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 21))
        self.menubar.setObjectName("menubar")
        Circles.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Circles)
        self.statusbar.setObjectName("statusbar")
        Circles.setStatusBar(self.statusbar)

        self.retranslateUi(Circles)
        QtCore.QMetaObject.connectSlotsByName(Circles)

    def retranslateUi(self, Circles):
        _translate = QtCore.QCoreApplication.translate
        Circles.setWindowTitle(_translate("Circles", "MainWindow"))
        self.make_circle.setText(_translate("Circles", "Круги"))


class Circles(QMainWindow, Ui_Circles):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.make_circle.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def draw_circle(self, qp):
        r = randint(10, 200)
        qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
        qp.drawEllipse(100, 100, r, r)
        qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
        qp.drawEllipse(400, 100, r, r)
        qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
        qp.drawEllipse(250, 200, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    ex.show()
    sys.exit(app.exec_())
