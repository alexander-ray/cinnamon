from project import app
from flask import render_template
from flask_login import login_required, current_user
from flask.views import View


class HomeController(View):
    decorators = [login_required]

    def dispatch_request(self):
        # Sort in reverse chronological order
        instances = list(sorted(current_user.spending_history.get_spending_instances(),
                                key=lambda x: x.date, reverse=True))
        return render_template('home.html', instances=instances)


app.add_url_rule('/home', view_func=HomeController.as_view('home'))

