
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel

class HeaderMenuItem(QWidget):
    def __init__(self, icon=None, label_text="Header", parent=None):
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
        label.setStyleSheet("color: #333333")  # Specific styling for the header
        main_layout.addWidget(label)

        self.setLayout(main_layout)
