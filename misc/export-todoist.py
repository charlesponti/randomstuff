import json
import os
from typing import List

import requests
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, Column, Integer, MetaData
from todoist.api import TodoistAPI

# Load environment variables
load_dotenv()

# Initialize app
app = Flask(__name__)

# Set SQLAlchemy databse URI
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

# Initialize db
db = SQLAlchemy(app)

# Create Todoist API client
api = TodoistAPI(os.environ.get("TODOIST_API_TOKEN"))


class Item(db.Model):
    __tablename__ = "items"
    project_id: int = db.Column(db.Integer)
    responsible_uid: int = db.Column(db.Integer)
    section_id: int = db.Column(db.Integer)
    sync_id: int = db.Column(db.Integer)
    user_id: int = db.Column(db.Integer)
    added_by_uid: int = db.Column(db.Integer)
    assigned_by_uid: int = db.Column(db.Integer)
    checked: int = db.Column(db.Integer)
    child_order: int = db.Column(db.Integer)
    collapsed: int = db.Column(db.Integer)
    content: str = db.Column(db.String)
    date_added: str = db.Column(db.String)
    date_completed: int = db.Column(db.Integer)
    day_order: int = db.Column(db.Integer)
    due: str = db.Column(db.String)
    has_more_notes: bool = db.Column(db.Boolean)
    id: int = db.Column(Integer, primary_key=True)
    in_history: int = db.Column(db.Integer)
    is_deleted: int = db.Column(db.Integer)
    labels: List[str] = db.Column(db.String)
    parent_id: int = db.Column(db.Integer)
    priority: int = db.Column(db.Integer)
    project: int = db.Column(db.String)


class Project(db.Model):
    __tablename__ = "projects"
    child_order: int = db.Column(db.Integer)
    collapsed: int = db.Column(db.Integer)
    color: int = db.Column(db.Integer,)
    has_more_notes: bool = db.Column(db.Boolean)
    id: int = db.Column(db.String, primary_key=True)
    is_archived: int = db.Column(db.Integer)
    is_deleted: int = db.Column(db.Integer)
    is_favorite: int = db.Column(db.Integer)
    name: str = db.Column(db.String)
    parent_id: int = db.Column(db.Integer)
    shared: bool = db.Column(db.Boolean)


# Drop tables
db.drop_all()
db.session.commit()

# Create new tables
db.create_all()
db.session.commit()

# Update local state
api.sync()

# Get projects and items
projects: list = api.state["projects"]
items = api.state["items"]

project_names = []
items_v2 = []
project_mappings = {}

# ----- Create all projects ----
for project in projects:
    project = Project(id=int(project["id"]), name=project["name"])
    db.session.add(project)

db.session.commit()
# ---------------------------

# ----- Create all items ----

for item in items:
    item = Item(content=item["content"], project=item["project_id"])
    db.session.add(item)

db.session.commit()
# ---------------------------


@app.route("/")
def get_lists():
    return Item.


if __name__ == "__main__":
    app.run()
