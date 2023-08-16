
from PyQt5.QtWidgets import QSplitter, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

class SplitPanel(QWidget):
    def __init__(self, left_widget, right_widget, orientation=Qt.Horizontal, parent=None):
        super().__init__(parent)

        # Create a splitter and set the orientation
        self.splitter = QSplitter(orientation)
        self.splitter.addWidget(left_widget)
        self.splitter.addWidget(right_widget)

        # Add the splitter to the layout
        layout = QVBoxLayout()
        layout.addWidget(self.splitter)
        self.setLayout(layout)

    def set_sizes(self, sizes):
        self.splitter.setSizes(sizes)
