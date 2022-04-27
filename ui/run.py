from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from brownie.network import accounts
from brownie import network

import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('PyQt5 Tut')

        self.label = QtWidgets.QLabel(self)
        self.label.setText('Hello World!')
        self.label.move(50, 50)
        network.connect('development')
        self.user = accounts[0]

        bt1 = QtWidgets.QPushButton(self)
        bt1.setText('Click Me!')
        bt1.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        self.label.setText(self.user.address)
        self.update()

    def update(self):
        self.label.adjustSize()


def clicked():
    print('Button Clicked!')


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()

    # p = project.load("../", name="TokenProject")
    # p.load_config(
    # token = Token.deploy("Test Token", "TST", 18, 1e21, {'from': accounts[0]})
    # print(token.address)
    # print(p.TokenProject)
    sys.exit(app.exec_())


window()
