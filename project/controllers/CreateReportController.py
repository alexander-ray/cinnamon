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
        """
        Handler for create report. Takes filename data from form and generates report with user's current report
        generator

        :return: Template
        """
        form = CreateReportForm(request.form,
                                filename=current_user.report_generator.default_filename)

        if request.method == 'POST' and form.validate_on_submit():
            current_user.report_generator.default_filename = str(form.filename.data)
            include_description = False
            if request.form.get('include_description'):
                include_description = True

            spending_instances = current_user.spending_history.spending_instances
            output = current_user.report_generator.generate_report(spending_instances, include_description)
            db.session.commit()
            return output
        return render_template('create_report.html',
                               form=form)


app.add_url_rule('/create_report', view_func=CreateReportController.as_view('create_report'))