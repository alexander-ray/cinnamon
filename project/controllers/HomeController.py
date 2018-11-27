from project import app
from flask import render_template
from flask_login import login_required, current_user
from flask.views import View


class HomeController(View):
    decorators = [login_required]

    def dispatch_request(self):
        """
        Handler for requests to homepage. Retrieves data from model and passes to view

        :return: Template
        """
        summary = current_user.summary_generator.summary_template_method()
        accounts = current_user.accounts
        instances = current_user.spending_history.spending_instances
        return render_template('home.html', summary=summary, accounts=accounts, instances=instances)


app.add_url_rule('/home', view_func=HomeController.as_view('home'))

