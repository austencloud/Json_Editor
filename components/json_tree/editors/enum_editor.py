
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox

class EnumEditor(QWidget):
    def __init__(self, value, enum_values, parent=None):
        super().__init__(parent)
        self.editing = False
        self.value = value
        self.enum_values = enum_values

        # Layout and widgets
        self.layout = QVBoxLayout()
        self.label = QLabel(self.value)
        self.comboBox = QComboBox()
        self.comboBox.addItems(self.enum_values)
        self.comboBox.setCurrentText(self.value)
        self.comboBox.hide()

        # Signals and slots
        self.comboBox.currentTextChanged.connect(self.change_value)
        self.comboBox.setDisabled(True)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.comboBox)
        self.setLayout(self.layout)

    def toggle_editing(self):
        self.editing = not self.editing
        if self.editing:
            self.comboBox.show()
            self.comboBox.setDisabled(False)
        else:
            self.comboBox.hide()
            self.comboBox.setDisabled(True)

    def change_value(self, new_value):
        self.value = new_value
        self.toggle_editing()

