from project import app
from project.controllers.forms import AddAccountForm
from project.models.Account import Account
from flask import Flask, render_template, redirect, request
from flask_login import login_required, current_user
from flask.views import View


class AddAccountController(View):
    methods = ['GET', 'POST']
    decorators = [login_required]

    def dispatch_request(self):
        form = AddAccountForm(request.form)
        if request.method == 'POST' and form.validate_on_submit():
            account_name = request.form['account']
            account = Account(account_name)
            current_user.accounts.append(account)
            return redirect('home')
        return render_template('add_account.html',
                               form=form)


app.add_url_rule('/add_account', view_func=AddAccountController.as_view('add_account'))