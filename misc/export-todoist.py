import json
import os

import requests
from flask import Flask
from todoist.api import TodoistAPI

from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

api = TodoistAPI(os.environ["TODOIST_API_TOKEN"])
# api = TodoistAPI(environ.get("TODOIST_API_TOKEN"))
api.sync()
print(api.state["projects"])


@app.route("/lists")
def get_lists():
    return json.dumps([])


if __name__ == "__main__":
    app.run()
