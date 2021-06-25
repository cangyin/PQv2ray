from components.node import Node
from components.utils import *
import components.generators as gen

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QComboBox
from typing import Callable

class QLinkedNodeComboBox(QComboBox):

    def __init__(self, parent: Optional[QWidget], groupCombo :QComboBox=None, selector :Callable=None) -> None:
        super().__init__(parent=parent)
        self.special_group_mapping = {}
        self.selector = selector
        self.groupCombo = groupCombo
        if groupCombo:
            self.link_comboBox(groupCombo)        

    def link_comboBox(self, groupCombo):
        if self.groupCombo:
            groupCombo.currentTextChanged[str].disconnect(self.on_groupChanged)
        self.groupCombo = groupCombo
        groupCombo.currentTextChanged[str].connect(self.on_groupChanged)

    def set_special_group_mapping(self, mapping):
        '''
        set special group <-> nodes mapping
        '''
        self.special_group_mapping.update(mapping)

    def set_selector(self, selector):
        self.selector = selector

    @pyqtSlot(str)
    def on_groupChanged(self, group_name):
        nodes = []
        if group_name in self.special_group_mapping:
            nodes = self.special_group_mapping[group_name]
        else:
            nodes = gen.get_nodes_in_group(gen.get_group_id(group_name))
            print(gen.get_group_id(group_name))

        if self.selector:
            nodes = [node for node in nodes if self.selector(node)]

        self.clear()
        for node in nodes:
            self.addItem(node.name, node)
