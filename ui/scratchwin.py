
# PyQt5 imports
from shutil import unregister_archive_format
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from ui.scratch import *

from components.utils import *


from pyqtconfig import ConfigManager


class ScratchWin(QMainWindow):
    def __init__(self, parent: Optional['QWidget']=None, flags: Union[QtCore.Qt.WindowFlags, QtCore.Qt.WindowType]=Qt.Dialog|Qt.MSWindowsFixedSizeDialogHint) -> None:
        super().__init__(parent=parent, flags=flags)
        ui = Ui_scratch()
        self.ui = ui
        ui.setupUi(self)
        
    def event_(self, event: QtCore.QEvent) -> bool:
        try:
            print(type(event), QCursor.pos())
            w = QApplication.widgetAt(QCursor.pos())
            print(event, type( w ), w.objectName())
        except:
            pass
        return super().event(event)

