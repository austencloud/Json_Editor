
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QCheckBox, QLabel

class CheckBoxMenuItem(QWidget):
    def __init__(self, checked=False, image=None, label_text="Checkbox", parent=None):
        super().__init__(parent)

        # Main layout
        main_layout = QHBoxLayout()

        # Checkbox for the menu item
        self.checkbox = QCheckBox(self)
        self.checkbox.setChecked(checked)
        main_layout.addWidget(self.checkbox)

        # Optional image (icon) for the menu item
        if image:
            image_label = QLabel(self)
            image_label.setPixmap(image)
            main_layout.addWidget(image_label)

        # Label for the menu item
        label = QLabel(label_text, self)
        main_layout.addWidget(label)

        self.setLayout(main_layout)
