from PyQt5.QtWidgets import QAbstractItemDelegate, QItemDelegate, QComboBox
from PyQt5.QtCore import Qt, QTimer
from components.repository import PictographSchema


class ExpandingComboBox(QComboBox):
    def showPopup(self):
        super(ExpandingComboBox, self).showPopup()  # Expand the combo box when shown


class ComboBoxDelegate(QItemDelegate):
    def __init__(self, json_tree, parent=None):
        super(ComboBoxDelegate, self).__init__(parent)
        self.json_tree = json_tree

    def createEditor(self, parent, option, index):
        editor = QComboBox(parent)
        item = self.json_tree.itemFromIndex(index)
        property_name = item.data(0, Qt.UserRole)[-1]

        schema = PictographSchema().schema
        if "enum" in schema["properties"].get(property_name, {}):
            valid_values = schema["properties"][property_name]["enum"]
            editor.addItems(valid_values)

        editor.showPopup()  # Expand the combo box immediately after creating it

        QTimer.singleShot(0, editor.showPopup)
        return editor
    
    def setEditorData(self, editor, index):
        rect = self.json_tree.visualRect(index)  # Get the visual rectangle of the item
        editor.setGeometry(rect)  # Set the geometry based on the item's visual rect

        # You may also initialize the editor's value here if needed
        value = index.model().data(index, Qt.EditRole) or ""
        editor.setCurrentText(value)