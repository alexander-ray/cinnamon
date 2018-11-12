from project import app
from flask import render_template
from flask_login import login_required, current_user
from flask.views import View


class HomeController(View):
    decorators = [login_required]

    def dispatch_request(self):
        instances = current_user.spending_history.get_spending_instances()
        return render_template('home.html', instances=instances)


app.add_url_rule('/home', view_func=HomeController.as_view('home'))

