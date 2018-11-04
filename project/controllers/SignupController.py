from project import app
from project.controllers.forms import SignupForm
from project.models.User import User
from project.models.UserInformation import UserInformation
from project.models.Address import Address
from flask import render_template, redirect, url_for, request, flash
from flask.views import View
from project import db


class SignupController(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        form = SignupForm(request.form)
        if request.method == 'POST' and form.validate_on_submit():
            info = UserInformation(int(form.income.data),
                                   Address(form.street_address.data,
                                           form.city.data,
                                           form.state.data,
                                           form.zip.data))
            user = User(form.username.data, form.password.data, info)
            db.session.add(user)
            db.session.commit()
            flash('Thanks for registering')
            return redirect(url_for('login'))
        return render_template('signup.html', form=form)


app.add_url_rule('/signup', view_func=SignupController.as_view('signup'))
