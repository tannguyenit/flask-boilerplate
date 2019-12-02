import os
import unittest
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask import current_app
from werkzeug.local import LocalProxy

from app import create_app, db
from app.api import api
from infrastructor.exceptions import errors

logger = LocalProxy(lambda: current_app.logger)

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(api)
app.register_blueprint(errors)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(debug=True, host="0.0.0.0", port=5000)


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
