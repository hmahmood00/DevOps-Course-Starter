from todo_app.todo_item import TodoItem
from todo_app.view_model import ViewModel

def test_view_model_todo_items():
    items_list = [
        TodoItem('1', 'Todo', 'A new todo'), 
        TodoItem('2', 'Doing', 'another item Im currently doing'), 
        TodoItem('3', 'Done', 'Completed item')
    ]

    view_model = ViewModel(items_list)

    todo_items = view_model.todo_items

    assert len(todo_items) == 1