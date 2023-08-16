
from PyQt5.QtWidgets import QWidget, QFrame, QVBoxLayout

class DividerMenuItem(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Main layout
        main_layout = QVBoxLayout()

        # Horizontal line as a divider
        divider = QFrame(self)
        divider.setFrameShape(QFrame.HLine)
        divider.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(divider)

        self.setLayout(main_layout)
