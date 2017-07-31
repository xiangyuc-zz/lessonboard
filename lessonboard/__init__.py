from flask import Flask
from lessonboard.extensions import db, bcrypt, migrate

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
bcrypt.init_app(app)
migrate.init_app(app, db)


import lessonboard.views
