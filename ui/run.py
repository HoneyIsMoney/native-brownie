from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import create_account
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('PyQt5 Tut')

        self.public_key_label = QtWidgets.QLabel(self)
        self.public_key_label.setText('Public Key:')
        self.public_key_label.move(50, 50)

        self.private_key_label = QtWidgets.QLabel(self)
        self.private_key_label.setText('Private Key:')
        self.private_key_label.move(50, 70)

        bt1 = QtWidgets.QPushButton(self)
        bt1.setText('Click Me!')
        bt1.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        keys = create_account.new()
        self.public_key_label.setText(keys['public'])
        self.private_key_label.setText(keys['private'])
        self.update()

    def update(self):
        self.public_key_label.adjustSize()
        self.private_key_label.adjustSize()


def clicked():
    print('Button Clicked!')


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
