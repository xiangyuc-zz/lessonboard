from flask import Flask
from lessonboard.extensions import db, bcrypt

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
bcrypt.init_app(app)


import lessonboard.views
