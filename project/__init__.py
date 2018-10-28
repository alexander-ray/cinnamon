from flask import Flask

# Example __init__ from https://github.com/salimane/flask-mvc/
app = Flask('project')
app.debug = True
from project.controllers import *