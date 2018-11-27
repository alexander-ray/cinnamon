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
        """
        Handler for adding spending instances. Populates default fields and drop down menus. Withdraws amount from
        specified account, creates a new spending instance.

        :return: Template
        """
        form = LogSpendingForm(request.form)

        # Add account choices to form
        form.account.choices = [(name, name) for name in current_user.account_names]

        form.spending_type.choices = [(name.value, name.value) for name in SpendingType]
        if request.method == 'POST' and form.validate_on_submit():
            amount = float(request.form['amount'])
            account_name = request.form['account']
            # Convert to date (not datetime)
            date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
            description = request.form['description']
            instance_type = request.form['spending_type']
            account = current_user.get_account(account_name)
            spending_instance = SpendingInstanceFactory.factory_method(amount,
                                                                       account,
                                                                       date,
                                                                       description,
                                                                       instance_type)
            account.withdraw(spending_instance.amount)


            current_user.spending_history.add_spending_instance(spending_instance)
            db.session.commit()
            return redirect('home')
        return render_template('log_spending.html',
                               form=form)


app.add_url_rule('/spend', view_func=SpendingController.as_view('spend'))
