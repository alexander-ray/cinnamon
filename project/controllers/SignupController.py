from project import app
from project.controllers.forms import SignupForm
from project.models.User import User
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from flask.views import View


class SignupController(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        form = SignupForm(request.form)
        if request.method == 'POST' and form.validate_on_submit():
            user = User(form.username.data, form.password.data, None)
            flash('Thanks for registering')
            return redirect(url_for('login'))
        return render_template('signup.html', form=form)


app.add_url_rule('/signup', view_func=SignupController.as_view('signup'))
