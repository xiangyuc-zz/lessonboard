from flask_script import Manager, Shell
from flask_migrate import MigrateCommand
from lessonboard import app
from lessonboard.extensions import db, migrate
from lessonboard import models


manager = Manager(app)


migrate.init_app(app, db)
manager.add_command('db', MigrateCommand)


def _make_context():
    return dict(app=app, db=db, models=models)


manager.add_command('shell', Shell(make_context=_make_context))


@manager.command
def db_create_all():
    db.init_app(app)
    db.create_all()


if __name__ == "__main__":
    manager.run()
