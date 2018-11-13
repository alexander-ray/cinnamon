from project import app
from project.controllers.forms import CreateReportForm
from flask import render_template, request
from flask_login import login_required, current_user
from flask.views import View


class CreateReportController(View):
    methods = ['GET', 'POST']
    decorators = [login_required]

    def dispatch_request(self):
        # display form
        form = CreateReportForm(request.form)
        if request.method == 'POST' and form.validate_on_submit():
            output = current_user.report_generator.generate_report(current_user.spending_history.get_spending_instances())
            return output
        return render_template('create_report.html',
                               form=form)


app.add_url_rule('/create_report', view_func=CreateReportController.as_view('create_report'))