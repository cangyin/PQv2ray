from sys import argv
from PyQt5.QtWidgets import QApplication

from ui import MainWindow


if __name__ == "__main__":
    app = QApplication(argv)

    win = MainWindow()
    win.show()

    exit(app.exec_())
