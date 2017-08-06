from flask import Flask
from lessonboard.extensions import db, bcrypt, migrate, login_manager

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
bcrypt.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)


import lessonboard.views  # nopep8
