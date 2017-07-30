from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    time_created = db.Column(db.DateTime)

    def __init__(self, name):
        self.name = name
        self.time_created = datetime.now()

    def __repr__(self):
        return '<Subject {}>'.format(self.name)
