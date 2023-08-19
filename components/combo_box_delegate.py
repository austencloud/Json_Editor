from PyQt5.QtWidgets import QAbstractItemDelegate, QItemDelegate, QComboBox
from PyQt5.QtCore import Qt, QTimer
from components.repository import PictographSchema


class ExpandingComboBox(QComboBox):
    def showPopup(self):
        super(ExpandingComboBox, self).showPopup()  # Expand the combo box when shown

    def mousePressEvent(self, event):
        if self.view().isVisible():
            self.hidePopup()  # Hide the combo box if it's already shown
        else:
            self.showPopup()  # Show the combo box if it's hidden
        super(ExpandingComboBox, self).mousePressEvent(event)  # Call the base implementation


class ComboBoxDelegate(QItemDelegate):
    VALUE_OFFSET = 105  # Distance from the left side to the beginning of the value part
    VALUE_PADDING = 30  # Additional padding for the value part


    def __init__(self, json_tree, parent=None):
        super(ComboBoxDelegate, self).__init__(parent)
        self.json_tree = json_tree


    def paint(self, painter, option, index):
        item = self.json_tree.itemFromIndex(index)
        if item and item.childCount() == 0:  # Only customize rendering for leaf nodes
            key, value = item.text(0).split(' - ')
            painter.save()

            # Draw the key part with the default font
            painter.drawText(option.rect.left(), option.rect.top(), self.VALUE_OFFSET, option.rect.height(),
                            Qt.AlignVCenter | Qt.AlignLeft, key)

            # Draw the value part with a bold font and additional padding
            value_font = painter.font()
            value_font.setBold(True)
            value_font.setPointSize(value_font.pointSize() + 3)  # Increase the font size
            painter.setFont(value_font)
            painter.drawText(option.rect.left() + self.VALUE_OFFSET + self.VALUE_PADDING, option.rect.top(),
                            option.rect.width() - self.VALUE_OFFSET - self.VALUE_PADDING, option.rect.height(),
                            Qt.AlignVCenter | Qt.AlignLeft, value)

            painter.restore()
        else:
            super(ComboBoxDelegate, self).paint(painter, option, index)  # Use default rendering for non-leaf nodes
        
            
    def createEditor(self, parent, option, index):
        item = self.json_tree.itemFromIndex(index)
        if item.childCount() == 0:  # Only create a combo box for leaf nodes
            editor = QComboBox(parent)
            key, value = item.text(0).split(' - ')
            property_name = item.data(0, Qt.UserRole)[-1]

            schema = PictographSchema().schema
            if "enum" in schema["properties"].get(property_name, {}):
                valid_values = schema["properties"][property_name]["enum"]
                editor.addItems(valid_values)
                editor.setCurrentText(value)  # Set the current text to the value part of the item's text

            editor.setProperty("keyPart", key)  # Store the key part of the text

            QTimer.singleShot(0, editor.showPopup)
            return editor

        return super(ComboBoxDelegate, self).createEditor(parent, option, index)

    def setModelData(self, editor, model, index):
        key = editor.property("keyPart")  # Retrieve the key part of the text
        value = editor.currentText()
        model.setData(index, f"{key} - {value}", Qt.EditRole) 
    
    def setEditorData(self, editor, index):
        item = self.json_tree.itemFromIndex(index)
        key, value = item.text(0).split(' - ')
        rect = self.json_tree.visualRect(index)  # Get the visual rectangle of the item

        # Adjust the rectangle to cover only the value part of the item, including padding
        rect.setLeft(rect.left() + self.VALUE_OFFSET + self.VALUE_PADDING)
        editor.setGeometry(rect)

        # Set the current text to the value part of the item's text
        editor.setCurrentText(value)