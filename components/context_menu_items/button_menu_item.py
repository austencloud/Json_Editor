
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class ButtonMenuItem(QWidget):
    def __init__(self, image=None, label_text="Button", disabled=False, click_handler=None, parent=None):
        super().__init__(parent)
        
        # Main layout
        main_layout = QVBoxLayout()
        
        # Optional image (icon) for the menu item
        if image:
            image_label = QLabel(self)
            image_label.setPixmap(image)
            main_layout.addWidget(image_label)
        
        # Button for the menu item
        self.button = QPushButton(label_text, self)
        self.button.setDisabled(disabled)
        if click_handler:
            self.button.clicked.connect(click_handler)
        main_layout.addWidget(self.button)

        self.setLayout(main_layout)
