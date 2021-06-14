
from typing import List
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

    def setNode(self, index :int, node :Node):
        item = QStandardItem(repr(node))
        item.setDropEnabled(False)
        item.setData(node, NodeDataRole)
        self.setItem(index, 0, item),

    def getNode(self, index) -> Node:
        itemData = self.itemData(self.index(index, 0))
        return itemData[NodeDataRole]

    def removeNode(self, index):
        self.removeRow(index)

    def removeNodes(self, start_index, count):
        self.removeRows(row=start_index, count=count)

    def appendNode(self, node :Node):
        self.insertRow(self.rowCount())
        self.setNode(self.rowCount() - 1, node)

    def getNodes(self, startIndex=0, count=0) -> List[Node]:
        assert(self.rowCount() == 0 or startIndex < self.rowCount())
        nodes = []
        count = count or self.rowCount() - startIndex
        for i in range(startIndex, startIndex + count):
            nodes.append(self.getNode(i))
        return nodes

    def resetNodes(self, nodes :Node):
        self.removeRows(0, self.rowCount())
        if nodes:
            self.insertRows(0, len(nodes))
            for i, node in enumerate(nodes):
                self.setNode(i, node)
