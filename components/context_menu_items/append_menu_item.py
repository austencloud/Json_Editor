
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QLineEdit, QHBoxLayout

class AppendMenuItem(QWidget):
    def __init__(self, image=None, label_text="Append", options=None, parent=None):
        super().__init__(parent)
        
        # Main layout
        main_layout = QVBoxLayout()
        
        # Optional image (icon) for the menu item
        if image:
            image_label = QLabel(self)
            image_label.setPixmap(image)
            main_layout.addWidget(image_label)
        
        # Label for the menu item
        label = QLabel(label_text, self)
        main_layout.addWidget(label)

        # Select dropdown for choosing the item to append
        self.select_dropdown = QComboBox(self)
        if options:
            self.select_dropdown.addItems(options)
        main_layout.addWidget(self.select_dropdown)

        # Conditional section for property name input
        property_layout = QHBoxLayout()
        property_name_label = QLabel("Property Name:", self)
        property_layout.addWidget(property_name_label)
        self.property_name_dropdown = QComboBox(self)
        # Add property name options if needed
        property_layout.addWidget(self.property_name_dropdown)
        self.property_name_input = QLineEdit(self)
        property_layout.addWidget(self.property_name_input)
        main_layout.addLayout(property_layout)

        self.setLayout(main_layout)
