from project import app
from project.controllers.forms import CreateReportForm
from flask import render_template, request
from flask_login import login_required, current_user
from flask.views import View
from project import db


class CreateReportController(View):
    methods = ['GET', 'POST']
    decorators = [login_required]

    def dispatch_request(self):
        # display form
        form = CreateReportForm(request.form,
                                filename=current_user.report_generator.filename)

        if request.method == 'POST' and form.validate_on_submit():
            current_user.report_generator.filename = str(form.filename.data)
            output = current_user.report_generator.generate_report(current_user.spending_history.get_spending_instances())
            db.session.commit()
            return output
        return render_template('create_report.html',
                               form=form)


app.add_url_rule('/create_report', view_func=CreateReportController.as_view('create_report'))