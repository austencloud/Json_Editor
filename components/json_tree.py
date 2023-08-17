from PyQt5.QtCore import Qt, pyqtSignal, QTimer
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem
from PyQt5.QtGui import QFont, QColor, QBrush
from functools import partial



class JsonTree(QTreeWidget):
    itemValueChanged = pyqtSignal(list, str)

    def __init__(self, parent=None):
        super(JsonTree, self).__init__(parent)
        self.itemChanged.connect(self.on_item_changed)
        self.itemCollapsed.connect(self.on_item_collapsed)
        self.json_data = {}

    def set_json(self, json_data):
        self.json_data = json_data
        self.clear()
        self.add_subnodes(None, json_data)
        
    def add_subnodes(self, parent, data, path=[]):
        if isinstance(data, list):
            for idx, group in enumerate(data):
                # Extract start and end positions
                start_position = group[0]["start_position"].replace("alpha", "α").replace("beta", "β").replace("gamma", "Γ")
                end_position = group[0]["end_position"].replace("alpha", "α").replace("beta", "β").replace("gamma", "Γ")

                # Create a new item with the start and end positions
                item = QTreeWidgetItem([f"{start_position}→{end_position}"])
                item.setData(0, Qt.UserRole, path + [idx])
                if parent is None:
                    self.addTopLevelItem(item)
                else:
                    parent.addChild(item)

                for sub_idx, sub_item in enumerate(group[1:]):
                    sub_key = ["Blue", "Red", "Optimal Location"][sub_idx] if sub_idx < 3 else str(sub_idx)
                    child_item = QTreeWidgetItem([sub_key])
                    child_item.setData(0, Qt.UserRole, path + [idx, sub_idx + 1])  # Use sub_idx + 1 instead of sub_key
                    if sub_key in ["Red", "Blue"]:
                        font = QFont()
                        font.setBold(True)
                        child_item.setFont(0, font)
                        color = QColor("red") if sub_key == "Red" else QColor("blue")
                        child_item.setForeground(0, QBrush(color))
                    item.addChild(child_item)

                    if isinstance(sub_item, dict):
                        self.add_subnodes(child_item, sub_item, path + [idx, sub_idx + 1])  # Corrected path here
                        if sub_key in ["Red", "Blue"]:
                            self.collapse_to_leaf_nodes(child_item)

        elif isinstance(data, dict):
            for key, value in data.items():
                item = QTreeWidgetItem([key])
                item.setData(0, Qt.UserRole, path + [key])
                if parent is None:
                    self.addTopLevelItem(item)
                else:
                    parent.addChild(item)
                self.add_subnodes(item, value, path + [key])
        else:
            item = QTreeWidgetItem([str(data)])
            item.setData(0, Qt.UserRole, path)
            item.setFlags(item.flags() | Qt.ItemIsEditable)  # Making the item editable
            if parent is None:
                self.addTopLevelItem(item)
            else:
                parent.addChild(item)

    def collapse_to_leaf_nodes(self, item):
        for i in range(item.childCount()):
            child = item.child(i)
            self.collapse_to_leaf_nodes(child)
            self.collapseItem(child)

    def on_item_collapsed(self, item):
        # Auto-collapse all sub-levels of the collapsed item
        for i in range(item.childCount()):
            child = item.child(i)
            self.collapseItem(child)

    def get_path_to_item(self, item):
        # Retrieve the path from the custom data
        return item.data(0, Qt.UserRole)

    def on_item_changed(self, item, column):
        if item.childCount() == 0:  # It's a leaf node
            path = item.data(0, Qt.UserRole)
            value = item.text(column)
            self.update_json_data(self.json_data, path, value)
    
    def update_json_data(self, json_data, path, value):
        # Access the outer list using the first key
        outer_list = json_data[path[0]]

        # Access the inner list using the second key
        inner_list = outer_list[path[1]]

        # Access the color object using the third key
        color_object = inner_list[path[2]]

        # Update the value using the fourth key
        color_object[path[-1]] = value

