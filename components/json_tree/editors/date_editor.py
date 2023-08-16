
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QDateEdit
from PyQt5.QtCore import QDate

class DateEditor(QWidget):
    def __init__(self, value, parent=None):
        super().__init__(parent)
        self.editing = False
        self.value = QDate.fromString(value, "yyyy-MM-dd")

        # Layout and widgets
        self.layout = QVBoxLayout()
        self.label = QLabel(self.value.toString("yyyy-MM-dd"))
        self.dateEdit = QDateEdit(self.value)
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit.hide()

        # Signals and slots
        self.dateEdit.dateChanged.connect(self.change_value)
        self.dateEdit.setDisabled(True)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.dateEdit)
        self.setLayout(self.layout)

    def toggle_editing(self):
        self.editing = not self.editing
        if self.editing:
            self.dateEdit.show()
            self.dateEdit.setDisabled(False)
        else:
            self.dateEdit.hide()
            self.dateEdit.setDisabled(True)

    def change_value(self, new_date):
        self.value = new_date
        self.toggle_editing()

