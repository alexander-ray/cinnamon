from flask import Flask
# Example __init__ from https://github.com/salimane/flask-mvc/
app = Flask('project')
# Why you need this, I'm not sure
app.config['SECRET_KEY'] = 'random'
app.debug = True

# https://github.com/maxcountryman/flask-login
# https://github.com/realpython/flask-registration/blob/master/project/__init__.py
import flask_login
login_manager = flask_login.LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# https://www.codementor.io/garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2
from flask_sqlalchemy import SQLAlchemy
import os
import project.models
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "database.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:////tmp/test.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


Base.metadata.create_all(bind=engine)
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xi-facelift
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

from project.models.User import User
from project.controllers import *

# Work with SQLAlchemy to get actual persistence going
user = User('billy', 'bob', None)
@login_manager.user_loader
def load_user(user_id):
    #return user
    return User.query.filter(User.username == 'admin').first()
