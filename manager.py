from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db


app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("db", MigrateCommand)
manager.add_command("runserver", Server(use_debugger=True))


@manager.command
def createdb():
    db.create_all()

if __name__ == '__main__':
    manager.run()
