from project import app
from project.controllers.forms import AddAccountForm
from project.models.Account import ConcreteAccount, AccountEmailDecorator, AccountSavingsDecorator
from flask import render_template, redirect, request, flash
from flask_login import login_required, current_user
from flask.views import View
from project import db


class AddAccountController(View):
    methods = ['GET', 'POST']
    decorators = [login_required]

    def dispatch_request(self):
        """
        Handler for add account controller. Takes data from account add form, creates new account with decorator classes

        :return: Template
        """
        form = AddAccountForm(request.form)
        if request.method == 'POST' and form.validate_on_submit():
            # create new account
            account_name = request.form['account']
            include_email = False
            include_savings = False

            if account_name in current_user.account_names:
                flash('Account already exists')
                return render_template('add_account.html', form=form)

            # https://stackoverflow.com/questions/31859903/
            if request.form.get('include_savings'):
                include_savings = True
            if request.form.get('include_email'):
                include_email = True
            account = ConcreteAccount(account_name)
            if include_savings:
                account = AccountSavingsDecorator(account)
            if include_email:
                account = AccountEmailDecorator(account)

            current_user.accounts.append(account)
            # commit changes to database
            db.session.commit()
            return redirect('home')
        return render_template('add_account.html',
                               form=form)


app.add_url_rule('/add_account', view_func=AddAccountController.as_view('add_account'))