
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox

class BooleanEditor(QWidget):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.editing = False
        self.value = value

        # Layout and widgets
        self.layout = QVBoxLayout()
        self.label = QLabel(":")
        self.comboBox = QComboBox()
        self.comboBox.addItems(["True", "False"])
        self.comboBox.setCurrentText(str(self.value))
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
        self.value = new_value == "True"
        self.toggle_editing()

