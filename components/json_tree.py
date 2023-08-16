from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem


class JsonTree(QTreeWidget):
    itemValueChanged = pyqtSignal(list, str)

    def __init__(self, parent=None):
        super(JsonTree, self).__init__(parent)
        self.itemChanged.connect(self.on_item_changed)
        self.json_data = {}  # Initialize json_data here


    def set_json(self, json_data):
        self.json_data = json_data
        self.clear()
        self.add_subnodes(None, json_data)

    def add_subnodes(self, parent, data, path=[]):
        if isinstance(data, dict):
            for key, value in data.items():
                item = QTreeWidgetItem([key])
                item.setData(0, Qt.UserRole, path + [key])
                if parent is None:
                    self.addTopLevelItem(item)
                else:
                    parent.addChild(item)
                self.add_subnodes(item, value, path + [key])
        elif isinstance(data, list):
            for idx, value in enumerate(data):
                item = QTreeWidgetItem([f"[{idx}]"])
                item.setData(0, Qt.UserRole, path + [idx])
                if parent is None:
                    self.addTopLevelItem(item)
                else:
                    parent.addChild(item)
                self.add_subnodes(item, value, path + [idx])
        else:
            item = QTreeWidgetItem([str(data)])
            item.setData(0, Qt.UserRole, path)
            if parent is None:
                self.addTopLevelItem(item)
            else:
                parent.addChild(item)

    def get_path_to_item(self, item):
        # Retrieve the path from the custom data
        return item.data(0, Qt.UserRole)

    def on_item_changed(self, item, column):
        if item.childCount() == 0:  # It's a leaf node
            path = self.get_path_to_item(item)
            value = item.text(column)
            self.update_json_data(path, value)
            self.itemValueChanged.emit(path, value)  # Emit the signal

    def update_json_data(self, path, value):
        target_data = self.json_data
        for key in path[:-1]:
            if isinstance(key, int):
                target_data = target_data[key]
            else:
                target_data = target_data[key]
        last_key = path[-1]
        target_data[last_key] = value
