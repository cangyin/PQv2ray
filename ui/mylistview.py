from typing import Iterable, Optional

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MyListView(QListView):
    
    focusIn = pyqtSignal()
    focusOut = pyqtSignal()
    keyPress = pyqtSignal(QKeyEvent)

    def __init__(self, parent: Optional[QWidget]) -> None:
        super().__init__(parent=parent)

    @pyqtSlot()
    def focusInEvent(self, e: QFocusEvent) -> None:
        self.focusIn.emit()
        return super().focusInEvent(e)

    @pyqtSlot()
    def focusOutEvent(self, e: QFocusEvent) -> None:
        self.focusOut.emit()
        return super().focusOutEvent(e)

    @pyqtSlot()
    def keyPressEvent(self, e: QKeyEvent) -> None:
        self.keyPress.emit(e)
        return super().keyPressEvent(e)