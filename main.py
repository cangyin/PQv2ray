import sys
from PyQt5.QtWidgets import QApplication

from ui import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)

    win = MainWindow()
    win.show()

    sys.exit(app.exec_())
