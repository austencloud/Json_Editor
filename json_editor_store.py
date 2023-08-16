
from datetime import datetime
import random
import json

class JsonEditorStore:
    def __init__(self, repository):
        self.selected_node = None
        self.repository = repository
        self.json_schema = None
        self.json_data = {}

    def generate_id(self):
        return str(datetime.now().timestamp()) + str(random.randint(1, 10000)).zfill(4)

    def validate_with_schema(self, schema, value):
        return True

    def set_json_data(self, data):
        self.json_data = data

    def get_json_data(self):
        return self.json_data

    def select_node(self, node):
        self.selected_node = node

    def get_selected_node(self):
        return self.selected_node
