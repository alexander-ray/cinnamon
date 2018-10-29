from flask import Flask
# Example __init__ from https://github.com/salimane/flask-mvc/
app = Flask('project')
# Why you need this, I'm not sure
app.config['SECRET_KEY'] = 'random'
app.debug = True
from project.controllers import *
