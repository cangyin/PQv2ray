
from typing import ItemsView, List
from components.utils import dump_jsons
from components.node import Node
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# item data roles for table model
DisplayRole = Qt.DisplayRole
NodeDataRole = Qt.UserRole


class NodeListModel(QStandardItemModel):

    def __init__(self, count, parent):
        super().__init__(count, 1, parent=parent)

    def _makeNodeItem(self, node :Node):
        item = QStandardItem(repr(node))
        item.setDropEnabled(False)
        item.setData(node, NodeDataRole)
        return item

    def count(self):
        return self.rowCount()

    def setNode(self, index :int, node :Node):
        self.setItem(index, 0, self._makeNodeItem(node)),

    def getNode(self, index) -> Node:
        itemData = self.itemData(self.index(index, 0))
        return itemData.get(NodeDataRole, Node())

    def removeNode(self, index :int):
        self.removeRow(index)

    def removeNodes(self, start_index :int, count :int):
        self.removeRows(row=start_index, count=count)

    def insertNode(self, index :int, node :Node):
        self.insertRow(index, self._makeNodeItem(node))

    def appendNode(self, node :Node):
        self.appendRow(self._makeNodeItem(node))

    def getNodes(self, startIndex :int=0, count :int=0) -> List[Node]:
        assert(self.count() == 0 or startIndex < self.count())
        nodes = []
        count = count or self.count() - startIndex
        for i in range(startIndex, startIndex + count):
            nodes.append(self.getNode(i))
        return nodes

    def resetNodes(self, nodes :List[Node]=[]):
        self.removeRows(0, self.count())
        if nodes:
            self.insertRows(0, len(nodes))
            for i, node in enumerate(nodes):
                self.setNode(i, node)
