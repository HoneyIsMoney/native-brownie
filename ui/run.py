from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import create_account


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui/ui.ui', self)
        self.show()

        self.searchButton.clicked.connect(self.on_click)

    def on_click(self, event):
        searchString = self.searchField.text()
        account = create_account.new(searchString)

        self.pubField.setText(account["public"])
        self.privField.setText(account["private"])


def main():
    app = QApplication([])
    window = MainWindow()
    app.exec_()


if __name__ == '__main__':
    main()
