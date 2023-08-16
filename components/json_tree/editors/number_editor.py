
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QDoubleSpinBox

class NumberEditor(QWidget):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.editing = False
        self.value = float(value)

        # Layout and widgets
        self.layout = QVBoxLayout()
        self.label = QLabel(str(self.value))
        self.doubleSpinBox = QDoubleSpinBox()
        self.doubleSpinBox.setValue(self.value)
        self.doubleSpinBox.hide()

        # Signals and slots
        self.doubleSpinBox.valueChanged.connect(self.change_value)
        self.doubleSpinBox.setDisabled(True)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.doubleSpinBox)
        self.setLayout(self.layout)

    def toggle_editing(self):
        self.editing = not self.editing
        if self.editing:
            self.doubleSpinBox.show()
            self.doubleSpinBox.setDisabled(False)
        else:
            self.doubleSpinBox.hide()
            self.doubleSpinBox.setDisabled(True)

    def change_value(self, new_value):
        self.value = new_value
        self.toggle_editing()

