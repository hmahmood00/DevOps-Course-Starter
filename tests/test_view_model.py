from todo_app.todo_item import TodoItem
from todo_app.view_model import ViewModel

def test_view_model_todo_items():
    items_list = [
        TodoItem('1', 'Todo', 'A new todo')
    ]

    view_model = ViewModel(items_list)

    todo_items = view_model.todo_items

    assert todo_items ## ===?????????