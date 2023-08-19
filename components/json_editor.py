from PyQt5.QtWidgets import QLabel, QMainWindow, QWidget, QApplication, QAction, QMenuBar, QFileDialog
from PyQt5.QtWidgets import QPushButton, QVBoxLayout
from PyQt5.QtCore import QTimer, Qt
from components.context_menu import ContextMenu, ContextMenuItem
from components.json_tree import JsonTree
from components.code_editor import CodeEditor
from components.split_panel import SplitPanel
import json


class JsonEditor(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.resize(1200, 1200)

        self.json_data = {}
        self.json_tree = JsonTree()
        self.code_editor = CodeEditor()
        self.current_file_path = None  # To keep track of the source file

        self.save_status_label = QLabel("")
        self.save_status_label.setMaximumHeight(20)
        self.save_status_label.setStyleSheet("font: 12pt")
        self.save_status_label.setAlignment(Qt.AlignCenter)

        self.split_panel = SplitPanel(self.json_tree, self.code_editor)
        self.split_panel.set_sizes([300, 500])

        layout = QVBoxLayout()
        layout.addWidget(self.save_status_label)  # Removed self.save_button
        layout.addWidget(self.split_panel)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.create_menu_bar()
        self.connect_signals()
        self.load_default_file()

    def load_default_file(self):
        self.current_file_path = 'pictographs.json'  # Set the path of the default file
        try:
            with open('pictographs.json', 'r') as file:
                self.json_data = json.load(file)  # Update this line
                self.json_tree.set_json(self.json_data)
                self.code_editor.set_code(json.dumps(self.json_data, indent=4))
        except Exception as e:
            print(f"Failed to load default file: {e}")

    def create_menu_bar(self):
        menu_bar = QMenuBar()
        file_menu = menu_bar.addMenu("File")
        
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_json_file)
        file_menu.addAction(open_action)

        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_json_file)
        file_menu.addAction(save_action)

        self.setMenuBar(menu_bar)

    def connect_signals(self):
        self.json_tree.itemChanged.connect(self.on_json_tree_item_changed)

    def on_json_tree_item_changed(self, item, column):
        path = self.json_tree.get_path_to_item(item)
        value = item.text(column)
        self.json_tree.update_json_data(self.json_data, path, value)
        self.code_editor.set_code(json.dumps(self.json_data, indent=4))
        self.save_json_file()  # Save the JSON file immediately after the edit

    def open_json_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open JSON File", "", "JSON Files (*.json);;All Files (*)", options=options)
        if file_path:
            with open(file_path, 'r') as file:
                self.json_data = json.load(file)
                self.current_file_path = file_path  
                self.json_tree.set_json(self.json_data)  # Update this line
                self.code_editor.set_code(json.dumps(self.json_data, indent=4))
                
    def save_json_file(self):
        if self.current_file_path:
            with open(self.current_file_path, 'w') as file:
                json.dump(self.json_data, file, indent=4)
            self.save_status_label.setText("File Saved!")
            QTimer.singleShot(5000, lambda: self.save_status_label.setText(""))  # Clear message after 5 seconds