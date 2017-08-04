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
    chapters = db.relationship('Chapter', backref='board', lazy='dynamic')

    def __init__(self, title, author_id, subject_id):
        self.title = title
        self.author_id = author_id
        self.subject_id = subject_id
        self.time_created = datetime.utcnow()

    def __repr__(self):
        return '<Board {}>'.format(self.title)


class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    time_created = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'))
    lessons = db.relationship('Lesson', backref='board', lazy='dynamic')

    def __init__(self, name, author_id, board_id):
        self.name = name
        self.author_id = author_id
        self.board_id = board_id
        self.time_created = datetime.utcnow()

    def __repr__(self):
        return '<Chapter {}>'.format(self.name)


class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    url = db.Column(db.String)
    comment = db.Column(db.Text)
    time_created = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id'))

    def __init__(self, title, url, comment, author_id, chapter_id):
        self.title = title
        self.url = url
        self.comment = comment
        self.author_id = author_id
        self.chapter_id = chapter_id
        self.time_created = datetime.utcnow()

    def __repr__(self):
        return '<Lesson {}>'.format(self.url)
