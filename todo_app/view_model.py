from todo_app.todo_item import TodoItem


class ViewModel:
    def __init__(self, items: "list[TodoItem]"):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def todo_items(self):
        
        return self._items

    @property
    def doing_items(self):
        return self._items

    @property
    def done_items(self):
        return self._items