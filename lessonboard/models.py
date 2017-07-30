from datetime import datetime
from lessonboard.extensions import db, bcrypt
from sqlalchemy.ext.hybrid import hybrid_property


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    _password = db.Column(db.String)
    time_created = db.Column(db.DateTime)

    @hybrid_property
    def password(self):
        return self._password

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.time_created = datetime.utcnow()

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @password.setter
    def _set_password(self, password):
        self._password = bcrypt.generate_password_hash(password)


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True)
    time_created = db.Column(db.DateTime)
    boards = db.relationship('Board', backref='subject', lazy='dynamic')

    def __init__(self, name):
        self.name = name
        self.time_created = datetime.utcnow()

    def __repr__(self):
        return '<Subject {}>'.format(self.name)


class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    time_created = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'))

    def __init__(self, title, author_id, subject_id):
        self.title = title
        self.author_id = author_id
        self.subject_id = subject_id
        self.time_created = datetime.utcnow()

    def __repr__(self):
        return '<Board {}>'.format(self.title)
