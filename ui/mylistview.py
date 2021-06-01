import typing

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QWidget

class MyListView(QtWidgets.QListView):
    
    focusIn = QtCore.pyqtSignal()
    focusOut = QtCore.pyqtSignal()

    def __init__(self, parent: typing.Optional[QWidget]) -> None:
        super().__init__(parent=parent)

    @QtCore.pyqtSlot()
    def focusInEvent(self, e: QtGui.QFocusEvent) -> None:
        self.focusIn.emit()
        return super().focusInEvent(e)

    @QtCore.pyqtSlot()
    def focusOutEvent(self, e: QtGui.QFocusEvent) -> None:
        self.focusOut.emit()
        return super().focusOutEvent(e)