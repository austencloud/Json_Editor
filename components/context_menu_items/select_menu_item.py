
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QComboBox, QLabel

class SelectMenuItem(QWidget):
    def __init__(self, items=[], selected_value=None, icon=None, label_text="Select", parent=None):
        super().__init__(parent)

        # Main layout
        main_layout = QHBoxLayout()

        # Optional image (icon) for the menu item
        if icon:
            image_label = QLabel(self)
            image_label.setPixmap(icon)
            main_layout.addWidget(image_label)

        # Label for the menu item
        label = QLabel(label_text, self)
        main_layout.addWidget(label)

        # Dropdown selection (combo box) for the menu item
        self.combo_box = QComboBox(self)
        for item in items:
            self.combo_box.addItem(item['label'], item['value'])
        if selected_value:
            self.combo_box.setCurrentIndex(self.combo_box.findData(selected_value))
        main_layout.addWidget(self.combo_box)

        self.setLayout(main_layout)
