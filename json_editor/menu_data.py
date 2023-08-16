
class MenuData:
    def __init__(self):
        self.menu_items = [
            {
                "name": "remove",
                "label": "Remove",
                "disabled": self.remove_disabled,
                "action": self.remove_action,
            }
        ]

    def remove_disabled(self, source):
        if source.node.parent:
            schema = source.node.parent.schema
            required = False
            if schema:
                if schema.required:
                    required = schema.required.index(source.node.name) >= 0
            return required
        else:
            return True

    def remove_action(self, source):
        source.remove()

menu_data = MenuData()
