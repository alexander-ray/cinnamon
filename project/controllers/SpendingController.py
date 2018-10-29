from project import app
from project.controllers.forms import LogSpendingForm
from project.models.User import User
from project.models.SpendingInstanceFactory import SpendingInstanceFactory
from flask import Flask, render_template, redirect, request
from flask_login import login_required, current_user
from flask.views import View


class SpendingController(View):
    methods = ['GET', 'POST']
    decorators = [login_required]

    def dispatch_request(self):
        form = LogSpendingForm(request.form)
        if request.method == 'POST' and form.validate_on_submit():
            amount = int(request.form['amount'])
            account = request.form['account']
            date = request.form['date']
            description = request.form['description']
            instance_type = request.form['spending_type']
            spending_instance = SpendingInstanceFactory.factory_method(amount,
                                                                       account,
                                                                       date,
                                                                       description,
                                                                       instance_type)
            print(spending_instance)
            current_user.spending_history.add_spending_instance(spending_instance)
            return redirect('home')
        return render_template('log_spending.html', form=form)


app.add_url_rule('/spend', view_func=SpendingController.as_view('spend'))