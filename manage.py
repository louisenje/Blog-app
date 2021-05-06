from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Role,Blog,Comments
from flask_migrate import Migrate,MigrateCommand


# Creating app instance
app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)

# migrations setts
migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)
# Tests 
@manager.command
def test():
    """
    run the unt tests
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

# shell
@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User,Role=Role,Blog=Blog,Comments=Comments)

if __name__ == '__main__':
    manager.run()