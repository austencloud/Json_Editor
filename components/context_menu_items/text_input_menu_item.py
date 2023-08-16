
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QLabel

class TextInputMenuItem(QWidget):
    def __init__(self, icon=None, label_text="Input", default_value="", parent=None):
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

        # Input text field for the menu item
        self.input_text = QLineEdit(self)
        self.input_text.setText(default_value)
        main_layout.addWidget(self.input_text)

        self.setLayout(main_layout)
