from flask import Flask, render_template, redirect, request, Response
from todo_app.flask_config import Config
from todo_app.todo_item import TodoItem
from todo_app.view_model import ViewModel
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import os

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    url = f"https://api.trello.com/1/boards/{os.getenv('TRELLO_BOARD_ID')}/cards"
    query = {
        'key': os.getenv("TRELLO_KEY"),
        'token': os.getenv("TRELLO_TOKEN")
    }

    response = requests.get(
    url,
    params=query
    )

    my_items = []

    trello_cards = (response.json()) #declare variable and add to the line below items_list
    for card in trello_cards:
        my_items.append(TodoItem.from_trello_card(card))

    item_view_model = ViewModel(my_items)
    return render_template('index.html', view_model=item_view_model)

@app.route('/addItem', methods =["POST"])
def add():
    name = request.form.get('new_todo_item') 
    url = "https://api.trello.com/1/cards"
    query = {
    'key': os.getenv("TRELLO_KEY"),
    'token': os.getenv("TRELLO_TOKEN"),
    'idList': os.getenv("TRELLO_TODO_IDLIST"),
    'name': name 
    }
    response = requests.request(
    "POST",
    url,
    params=query
    )
    return redirect ("/")

@app.route('/doingItem/<id>', methods =["POST"])
def doing_item(id):
    url = f"https://api.trello.com/1/cards/{id}"
    query = {
        'key': os.getenv("TRELLO_KEY"),
        'token': os.getenv("TRELLO_TOKEN"),
        'idList': os.getenv("TRELLO_DOING_IDLIST"),
    }
    response = requests.request(
    "PUT",
    url,
    params=query
    )
    return redirect ("/")

@app.route('/completeItem/<id>', methods =["POST"])
def complete_item(id):
    url = f"https://api.trello.com/1/cards/{id}"
    query = {
        'key': os.getenv("TRELLO_KEY"),
        'token': os.getenv("TRELLO_TOKEN"),
        'idList': os.getenv("TRELLO_COMPLETE_IDLIST"),
    }
    response = requests.request(
    "PUT",
    url,
    params=query
    )
    return redirect ("/")

if __name__ == '__main__':
    app.run()

