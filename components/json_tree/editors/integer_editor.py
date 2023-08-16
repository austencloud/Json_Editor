
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpinBox

class IntegerEditor(QWidget):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.editing = False
        self.value = int(value)

        # Layout and widgets
        self.layout = QVBoxLayout()
        self.label = QLabel(str(self.value))
        self.spinBox = QSpinBox()
        self.spinBox.setValue(self.value)
        self.spinBox.hide()

        # Signals and slots
        self.spinBox.valueChanged.connect(self.change_value)
        self.spinBox.setDisabled(True)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.spinBox)
        self.setLayout(self.layout)

    def toggle_editing(self):
        self.editing = not self.editing
        if self.editing:
            self.spinBox.show()
            self.spinBox.setDisabled(False)
        else:
            self.spinBox.hide()
            self.spinBox.setDisabled(True)

    def change_value(self, new_value):
        self.value = new_value
        self.toggle_editing()

