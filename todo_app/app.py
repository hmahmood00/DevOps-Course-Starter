from flask import Flask, render_template, redirect, request, Response
from todo_app.flask_config import Config
from todo_app.cards import TodoItem
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import os

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
    url = "https://api.trello.com/1/boards/MFxbg4oi/cards"
    query = {
        'key': os.getenv("TRELLO_KEY"),
        'token': os.getenv("TRELLO_TOKEN")
    }

    response = requests.get(
    url,
    params=query
    )

    myItems = []

    trello_items = (response.json()) #declare variable and add to the line below items_list
    for item in trello_items:
        if item["idList"] == '5ff3a8b1997284580b7a4fcc':
            item["status"] = "Done"
        elif item["idList"] == '5ff3a8b1997284580b7a4fcb':
            item["status"] = "Doing"
        else: item["status"] = "Todo"
        myItems.append(TodoItem(item['id'], item['status'], item['name']))
    return render_template("index.html", items = myItems)

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

