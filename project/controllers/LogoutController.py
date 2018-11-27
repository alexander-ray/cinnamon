from project import app
from flask import redirect
from flask_login import logout_user
from flask.views import View


class LogoutController(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        """
        Handler for logout

        :return: Redirect to login page
        """
        logout_user()
        return redirect('login')


app.add_url_rule('/logout', view_func=LogoutController.as_view('logout'))
