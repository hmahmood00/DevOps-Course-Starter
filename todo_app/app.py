from flask import Flask, render_template, redirect, request, Response
import todo_app.data.session_items as session
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

        elif item["idList"] == '5ff3a8b1997284580b7a4fcb':
            item["status"] = "Doing"

        else: item["status"] = "Todo"
    return render_template("index.html", items = trello_items)

@app.route('/addItem', methods =["POST"])
def add():
    title = request.form.get('new_todo_item')
    session.add_item(title)
    return redirect ("/")

@app.route('/completeItem/<id>', methods =["POST"])
def complete_item(id):
    converted_id = int(id)
    item = session.get_item(converted_id)
    item["status"] = "Completed"
    session.save_item(item)
    return redirect ("/")

if __name__ == '__main__':
    app.run()

