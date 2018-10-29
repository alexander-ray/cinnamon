from flask import Flask
# Example __init__ from https://github.com/salimane/flask-mvc/
app = Flask('project')
# Why you need this, I'm not sure
app.config['SECRET_KEY'] = 'random'
app.debug = True

# https://github.com/maxcountryman/flask-login
# https://github.com/realpython/flask-registration/blob/master/project/__init__.py
import flask_login
from project.models.User import User
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User('billy', 'bob', None)


from project.controllers import *
