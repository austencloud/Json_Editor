
from PyQt5.QtCore import QObject, pyqtSignal

class JsonTreeStore(QObject):
    data_changed = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self._data = None

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data
        self.data_changed.emit()

    data = property(get_data, set_data)
