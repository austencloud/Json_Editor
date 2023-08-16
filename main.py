from PyQt5.QtWidgets import QApplication
from components.json_editor import JsonEditor

def main():
    app = QApplication([])
    json_editor = JsonEditor()
    json_editor.show()
    app.exec_()

if __name__ == "__main__":
    main()
