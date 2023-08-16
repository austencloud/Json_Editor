
from PyQt5.QtWidgets import QAction, QMenu, QApplication
from PyQt5.QtCore import Qt

class ContextMenuItem(QAction):
    def __init__(self, label, parent, action=None, submenu=None):
        super().__init__(label, parent)
        self.label = label
        self.action = action
        self.submenu = submenu
        
        # Connect the action if provided
        if action:
            self.triggered.connect(action)
            
        # Add submenu if provided
        if submenu:
            self.setMenu(submenu)

class ContextMenu(QMenu):
    def __init__(self, title, parent=None):
        super().__init__(title, parent)

    def add_item(self, label, action=None, submenu=None):
        item = ContextMenuItem(label, self, action, submenu)
        self.addAction(item)
        return item

    def add_divider(self):
        self.addSeparator()

    def show_at(self, pos):
        self.exec_(pos)

