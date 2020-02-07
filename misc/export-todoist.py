import json

import requests
from flask import Flask
from todoist.api import TodoistAPI

app = Flask(__name__)

app.

api = TodoistAPI('0123456789abcdef0123456789abcdef01234567')
api.sync()
print(api.state['projects'])

@app.route("/lists")
def get_lists():
    return json.dumps([])


if __name__ == "__main__":
    app.run()
