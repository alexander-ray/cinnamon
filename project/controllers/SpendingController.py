from project import app
from project.controllers.forms import LogSpendingForm
from project.models.SpendingInstanceFactory import SpendingInstanceFactory
from project.models.SpendingType import SpendingType
from flask import render_template, redirect, request
from flask_login import login_required, current_user
from flask.views import View
from project import db
from datetime import datetime


class SpendingController(View):
    methods = ['GET', 'POST']
    decorators = [login_required]

    def dispatch_request(self):
        # Create basic logging form
        form = LogSpendingForm(request.form)

        # Add account choices to form
        form.account.choices = [(name, name) for name in current_user.get_account_names()]

        # TODO:
        # Do something cooler with account balances, etc
        # Add spending type choices to form
        form.spending_type.choices = [(name.value, name.value) for name in SpendingType]
        if request.method == 'POST' and form.validate_on_submit():
            amount = float(request.form['amount'])
            account = request.form['account']
            # Convert to date (not datetime)
            date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
            description = request.form['description']
            instance_type = request.form['spending_type']
            spending_instance = SpendingInstanceFactory.factory_method(amount,
                                                                       current_user.get_account(account),
                                                                       date,
                                                                       description,
                                                                       instance_type)
            current_user.get_account(account).withdraw(amount)
            current_user.spending_history.add_spending_instance(spending_instance)
            db.session.commit()
            return redirect('home')
        return render_template('log_spending.html',
                               form=form)


app.add_url_rule('/spend', view_func=SpendingController.as_view('spend'))
