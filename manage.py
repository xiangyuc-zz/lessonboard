from flask_script import Manager
from flask_migrate import MigrateCommand
from lessonboard import app
from lessonboard.extensions import db, migrate


manager = Manager(app)


migrate.init_app(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def db_create_all():
    db.init_app(app)
    db.create_all()


if __name__ == "__main__":
    manager.run()
