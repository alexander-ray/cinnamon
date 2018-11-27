from project import app
from project.controllers.forms import BaseUserForm
from project.models.User import User
from flask import render_template, redirect, request, flash
from flask_login import login_user
from flask.views import View
from project import bcrypt

class LoginController(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        """
        Login handler. Compares username and password to database, sends to homepage if approved

        :return: Template
        """
        form = BaseUserForm(request.form)
        if request.method == 'POST' and form.validate_on_submit():
            # https://github.com/realpython/flask-registration/blob/master/project/user/views.py
            user = User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect('home')
            flash('Incorrect email or password')
            return render_template('login.html', form=form)
        return render_template('login.html', form=form)


app.add_url_rule('/login', view_func=LoginController.as_view('login'))
