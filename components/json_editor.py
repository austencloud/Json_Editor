
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMenuBar, QFileDialog
from components.context_menu import ContextMenu, ContextMenuItem
from components.json_tree import JsonTree
from components.code_editor import CodeEditor
from components.split_panel import SplitPanel
import json

class JsonEditor(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.json_data = {}
        self.json_tree = JsonTree()
        self.code_editor = CodeEditor()
        self.split_panel = SplitPanel(self.json_tree, self.code_editor)
        self.split_panel.set_sizes([300, 500])

        self.setCentralWidget(self.split_panel)
        self.create_menu_bar()
        self.connect_signals()

    def create_menu_bar(self):
        menu_bar = QMenuBar()
        file_menu = menu_bar.addMenu("File")
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_json_file)
        file_menu.addAction(open_action)
        self.setMenuBar(menu_bar)

    def connect_signals(self):
        self.json_tree.itemChanged.connect(self.on_json_tree_item_changed)

    def on_json_tree_item_changed(self, item, column):
        path = self.json_tree.get_path_to_item(item)
        value = item.text(column)
        self.json_tree.update_json_data(path, value)
        self.code_editor.set_code(json.dumps(self.json_data, indent=4))

    def open_json_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open JSON File", "", "JSON Files (*.json);;All Files (*)", options=options)
        if file_path:
            with open(file_path, 'r') as file:
                self.json_data = json.load(file)
                self.json_tree.json_data = self.json_data
                self.json_tree.clear()
                self.json_tree.add_subnodes(None, self.json_data)
                self.code_editor.set_code(json.dumps(self.json_data, indent=4)) 
