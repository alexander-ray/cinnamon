from project import app
from project.controllers.forms import SettingsForm
from project.models.UserInformation import UserInformation
from project.models.Address import Address
from flask import render_template, redirect, request
from flask_login import login_required, current_user
from flask.views import View
from project import db
from project.models.ReportType import ReportType
from project.models.ReportGenerator import CSVReportGenerator, JSONReportGenerator

class SettingsController(View):
    methods = ['GET', 'POST']
    decorators = [login_required]

    def dispatch_request(self):
        # display form
        # For some reason this setting defaults works
        # https://stackoverflow.com/questions/12099741/
        form = SettingsForm(request.form,
                            street_address=current_user.information.address.street_address,
                            city=current_user.information.address.city,
                            state=current_user.information.address.state,
                            zip=current_user.information.address.zip,
                            income=current_user.information.income,
                            )
        # Add report type choices to form
        form.report_type.choices = [(name.value, name.value) for name in ReportType]

        if request.method == 'POST' and form.validate_on_submit():
            info = UserInformation(int(form.income.data),
                                   Address(form.street_address.data,
                                           form.city.data,
                                           form.state.data,
                                           form.zip.data))

            # TODO:
            # Add additional options for report generation
            #   (include "created" timestamp, descriptions optionally, etc)
            # Update report generator type choice
            curr_filename = current_user.report_generator.filename
            if form.report_type.data == ReportType.CSV.value:
                current_user.report_generator = CSVReportGenerator(filename=curr_filename)
            else:
                current_user.report_generator = JSONReportGenerator(filename=curr_filename)

            current_user.information = info
            # commit changes to database
            db.session.commit()
            return redirect('home')
        return render_template('settings.html',
                               form=form)


app.add_url_rule('/settings', view_func=SettingsController.as_view('settings'))