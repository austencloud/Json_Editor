
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit

class StringEditor(QWidget):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.editing = False
        self.value = value

        # Layout and widgets
        self.layout = QVBoxLayout()
        self.label = QLabel(self.value)
        self.lineEdit = QLineEdit(self.value)
        self.lineEdit.hide()

        # Signals and slots
        self.lineEdit.textChanged.connect(self.change_value)
        self.lineEdit.setDisabled(True)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.lineEdit)
        self.setLayout(self.layout)

    def toggle_editing(self):
        self.editing = not self.editing
        if self.editing:
            self.lineEdit.show()
            self.lineEdit.setDisabled(False)
        else:
            self.lineEdit.hide()
            self.lineEdit.setDisabled(True)

    def change_value(self, new_value):
        self.value = new_value
        self.toggle_editing()
