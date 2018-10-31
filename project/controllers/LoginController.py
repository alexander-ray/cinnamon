from project import app
from project.controllers.forms import BaseUserForm
from project.models.User import User
from flask import render_template, redirect, request
from flask_login import login_user
from flask.views import View


class LoginController(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        form = BaseUserForm(request.form)
        user = User('tmp', 'tmp', None)
        if request.method == 'POST' and form.validate_on_submit():
            login_user(user)
            return redirect('home')
        return render_template('login.html', form=form)


app.add_url_rule('/login', view_func=LoginController.as_view('login'))