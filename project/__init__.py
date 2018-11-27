from flask import Flask
from flask_mail import Mail
from flask_bcrypt import Bcrypt

# Example __init__ from https://github.com/salimane/flask-mvc/
app = Flask('project')
mail = Mail(app)
bcrypt = Bcrypt(app)

# Why you need this, I'm not sure
app.config['SECRET_KEY'] = 'random'
app.debug = True

# https://github.com/maxcountryman/flask-login
# https://github.com/realpython/flask-registration/blob/master/project/__init__.py
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
import flask_login
login = flask_login.LoginManager()
login.init_app(app)
login.login_view = 'login'

# https://www.codementor.io/garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))
database_file = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xi-facelift
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

from project.controllers import *
import project.models
db.create_all()
from project.models.User import User


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# https://stackoverflow.com/questions/18401287/sphinx-file-not-found-sys-path-issue
import os
curr_directory = os.path.dirname(__file__)
with open(os.path.join(curr_directory, 'config.txt')) as f:
    username = next(f)
    password = next(f)

# http://flask.pocoo.org/snippets/85/
app.config.update(
MAIL_SERVER='smtp.gmail.com',
MAIL_PORT=587,
MAIL_USE_SSL=False,
MAIL_USE_TLS=True,
MAIL_USERNAME=username,
MAIL_PASSWORD=password
)
mail = Mail(app)

bcrypt = Bcrypt(app)

