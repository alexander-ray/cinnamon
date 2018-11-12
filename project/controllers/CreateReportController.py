from project import app
from project.controllers.forms import CreateReportForm
from flask import render_template, redirect, request, make_response
from flask_login import login_required, current_user
from flask.views import View
from io import StringIO
import csv


class CreateReportController(View):
    methods = ['GET', 'POST']
    decorators = [login_required]

    def dispatch_request(self):
        # display form
        form = CreateReportForm(request.form)
        if request.method == 'POST' and form.validate_on_submit():
            # Code for generating csv
            # https://stackoverflow.com/questions/11914472/
            # https://stackoverflow.com/questions/26997679/
            sio = StringIO()
            writer = csv.writer(sio)
            instances = current_user.spending_history.get_spending_instances()
            # Float formatting
            # Make nested list for writerows
            instances = [[i.__str__(), '{0:.2f}'.format(i.amount), i.account.name, i.date] for i in instances]
            writer.writerows(instances)
            output = make_response(sio.getvalue())
            output.headers["Content-Disposition"] = "attachment; filename=export.csv"
            output.headers["Content-type"] = "text/csv"
            return output
        return render_template('create_report.html',
                               form=form)


app.add_url_rule('/create_report', view_func=CreateReportController.as_view('create_report'))