from flask_script import Manager
from lessonboard import app
from lessonboard.models import db


manager = Manager(app)


@manager.command
def db_create_all():
    db.init_app(app)
    db.create_all()


if __name__ == "__main__":
    manager.run()
