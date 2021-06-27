from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from components.utils import *


class TextContentForm(QDialog):
    def __init__(self, parent: Optional[QWidget], title='', flags: Union[Qt.WindowFlags, Qt.WindowType]=Qt.Dialog) -> None:
        super().__init__(parent=parent, flags=flags)
        self.resize(600, 500)
        self.setWindowTitle(title)

        self.label = QLabel(self)
        self.plainTextEdit = QPlainTextEdit(self)
        self.plainTextEdit.setWordWrapMode(QTextOption.WordWrap)
        self.plainTextEdit.setVisible(False)
        self.plainTextEdit.setObjectName('TextContentForm-plainTextEdit')

        self.textEdit = QTextEdit(self)
        self.textEdit.setWordWrapMode(QTextOption.WordWrap)
        self.textEdit.setVisible(False)
        self.textEdit.setObjectName('TextContentForm-textEdit')

        self.btn_ok = QPushButton('好', self)
        self.btn_ok.setMinimumHeight(35)

        self.vlayout = QVBoxLayout(self)
        self.vlayout.addWidget(self.label)
        self.vlayout.addWidget(self.plainTextEdit)
        self.vlayout.addWidget(self.textEdit)
        self.vlayout.addWidget(self.btn_ok)

        self.btn_ok.clicked.connect(self.on_btn_ok_cliked)

    def on_btn_ok_cliked(self):
        self.accept()
