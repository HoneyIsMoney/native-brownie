from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('PyQt5 Tut')

        self.label = QtWidgets.QLabel(self)
        self.label.setText('Hello World!')
        self.label.move(50, 50)

        bt1 = QtWidgets.QPushButton(self)
        bt1.setText('Click Me!')
        bt1.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        print('Button Clicked!')
        self.label.setText('The Button Was Clicked!')
        self.update()

    def update(self):
        self.label.adjustSize()


def clicked():
    print('Button Clicked!')


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    print('working')
    sys.exit(app.exec_())


window()
