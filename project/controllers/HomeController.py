from project import app
from project.controllers.forms import SignupForm, BaseUserForm
from project.models.User import User
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from flask.views import View


class HomeController(View):
    decorators = [login_required]

    def dispatch_request(self):
        return render_template('home.html')


app.add_url_rule('/home', view_func=HomeController.as_view('home'))

