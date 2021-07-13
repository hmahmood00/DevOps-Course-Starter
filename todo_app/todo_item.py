import os

class TodoItem:
    #creating my to do items class
    def __init__(self, id, status, name):
        #initialising attributes
        self.id = id
        self.status = status
        self.name = name

    @classmethod
    def from_trello_card(cls, card):
        id = card['id']
        name = card['name']
        status = ''

        if card["idList"] == os.getenv('TRELLO_COMPLETE_IDLIST'):
            status = "Done"
        elif card["idList"] == os.getenv('TRELLO_DOING_IDLIST'):
            status = "Doing"
        else: status = "Todo"

        return cls(id, status, name)


