from flask import Flask, render_template, redirect, request, Response
from todo_app.flask_config import Config
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


    

    trello_items = (response.json()) #declare variable and add to the line below items_list
    for item in trello_items:
        if item["idList"] == '5ff3a8b1997284580b7a4fcc':
            item["status"] = "Done"
        else: item["status"] = "Todo"
    return render_template("index.html", items = trello_items)

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

@app.route('/completeItem/<id>', methods =["POST"])
def complete_item(id):
    converted_id = int(id)
    item = request.get_item(converted_id)
    item["status"] = "Completed"
    request.save_item(item)
    return redirect ("/")

if __name__ == '__main__':
    app.run()

