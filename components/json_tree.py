
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem
from PyQt5.QtGui import QFont, QColor, QBrush


class JsonTree(QTreeWidget):
    def __init__(self, parent=None):
        super(JsonTree, self).__init__(parent)
        self.itemChanged.connect(self.on_item_changed)
        self.itemExpanded.connect(self.on_item_expanded)
        self.json_data = {}

    def set_json(self, json_data):
        self.json_data = json_data
        self.clear()
        self.add_subnodes(None, json_data)

    def add_subnodes(self, parent, data, path=[]):
        if isinstance(data, list):
            for idx, group in enumerate(data):
                start_position = group[0]["start_position"].replace("alpha", "α").replace("beta", "β").replace("gamma", "Γ")
                end_position = group[0]["end_position"].replace("alpha", "α").replace("beta", "β").replace("gamma", "Γ")
                item = QTreeWidgetItem([f"{start_position}→{end_position}"])
                item.setData(0, Qt.UserRole, path + [idx])
                if parent is None:
                    self.addTopLevelItem(item)
                else:
                    parent.addChild(item)
                for sub_idx, sub_item in enumerate(group[1:]):
                    sub_key = ["Left", "Right", "Optimal Location"][sub_idx] if sub_idx < 3 else str(sub_idx)
                    child_item = QTreeWidgetItem([sub_key])
                    child_item.setData(0, Qt.UserRole, path + [idx, sub_idx + 1])
                    if sub_key in ["Left", "Right"]:
                        font = QFont()
                        font.setBold(True)
                        child_item.setFont(0, font)
                        color = QColor("blue") if sub_key == "Left" else QColor("red")
                        child_item.setForeground(0, QBrush(color))
                    item.addChild(child_item)  # Moved inside the loop
                    if isinstance(sub_item, dict):
                        self.add_subnodes(child_item, sub_item, path + [idx, sub_idx + 1])

        elif isinstance(data, dict):
            for key, value in data.items():
                if key == "color":  # Skip the "color" attribute
                    continue
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
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            font = QFont()
            font.setBold(True)
            font.setPointSize(font.pointSize() + 3)
            item.setFont(0, font)
            if parent is None:
                self.addTopLevelItem(item)
            else:
                parent.addChild(item)


    def on_item_expanded(self, item):
        item_text = item.text(0)
        if 'α' in item_text or 'β' in item_text or 'Γ' in item_text:
            self.expand_red_blue_nodes(item)

    def expand_red_blue_nodes(self, item):
        for i in range(item.childCount()):
            child = item.child(i)
            child_text = child.text(0)
            if child_text in ["Left", "Right"]:
                self.expandItem(child)
                self.expand_leaf_nodes(child)

    def expand_leaf_nodes(self, item):
        for i in range(item.childCount()):
            child = item.child(i)
            self.expandItem(child)
            self.expand_leaf_nodes(child)

    def get_path_to_item(self, item):
        return item.data(0, Qt.UserRole)

    def on_item_changed(self, item, column):
        if item.childCount() == 0:
            path = item.data(0, Qt.UserRole)
            value = item.text(column)
            self.update_json_data(self.json_data, path, value)

    def update_json_data(self, json_data, path, value):
        outer_list = json_data[path[0]]
        inner_list = outer_list[path[1]]
        color_object = inner_list[path[2]]
        color_object[path[-1]] = value
