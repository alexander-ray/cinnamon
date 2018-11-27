from project import db
from abc import abstractmethod, ABCMeta
from flask_login import current_user
import datetime


class SummaryGenerator(db.Model):
    __metaclass__ = ABCMeta

    __tablename__ = 'summary_generator'

    _id = db.Column(db.Integer, primary_key=True)
    _type = db.Column(db.String(80))
    _user_id = db.Column(db.Integer, db.ForeignKey('user._id'))

    def summary_template_method(self):
        """
        Template method for summary generator. Enforces ordering of summary generation using the template method
        design pattern

        :return: HTML-formatted string
        """
        ret = ''
        ret += self._get_greeting()
        ret += self._get_col(current_user.information.address.state)
        ret += self._get_summary()
        return ret

    def _get_greeting(self):
        """
        Method to generate generic greeting for user's summary

        :return: HTML-formatted string
        """
        return '<p>Hi! Here\'s how your spending looks!</p>'

    def _get_col(self, state):
        """
        Method for (rough) state COL lookup

        :param state: Two letter state abbreviation, as a string
        :return: HTML-formatted cost-of-living string
        """
        fmt = '<p><b>Your cost of living:</b> '
        if state in ('CA', 'NY'):
             fmt += 'high'
        elif state in ('WA', 'OR', 'CO', 'MA'):
            fmt += 'medium'
        else:
            fmt += 'low'
        fmt += '. '
        fmt += '<em>Make sure you keep this in mind as you spend!</em></p>'
        return fmt

    @abstractmethod
    def _get_summary(self):
        """
        Abstract summary method, to be implemented by subclasses

        :return: HTML-formatted string
        """
        return

    __mapper_args__ = {
        'polymorphic_identity': 'summary_generator',
        'polymorphic_on': _type
    }


class TotalExpenditureSummaryGenerator(SummaryGenerator):
    def _get_summary(self):
        """
        Total expenditure summary method. Uses accounts to get a holistic, overall view of spending

        :return: HTML-formatted string
        """
        ret = ''
        ret += '<p><b>Income:</b> $' + '{0:.2f}'.format(current_user.information.income) + '</p>'
        ret += '<p><b>Total Expenditure:</b> $' + '{0:.2f}'.format(sum([a.expenditure for a in current_user.accounts])) + '</p>'
        return ret

    __mapper_args__ = {
        'polymorphic_identity': 'total_expenditure_report_generator',
    }


class DateOrientedSummaryGenerator(SummaryGenerator):
    def _get_summary(self):
        """
        Date-oriented summary method. Uses spending history to show spending over the past month, year, and all time

        :param user: User for use generating summary
        :return: HTML-formatted string
        """
        spending_in_past_month = [si.amount for si in current_user.spending_history.spending_instances
                                  if (datetime.date.today() - si.date).days <= 30]
        spending_in_past_year = [si.amount for si in current_user.spending_history.spending_instances
                                  if (datetime.date.today() - si.date).days <= 30*12]
        spending_all_time = [si.amount for si in current_user.spending_history.spending_instances]
        ret = '<p>Spending, including money saved:</p>'

        ret += '<p><b>Spending in past month:</b> $' + '{0:.2f}'.format(sum(spending_in_past_month)) + '</p>'
        ret += '<p><b>Spending in past year:</b> $' + '{0:.2f}'.format(sum(spending_in_past_year)) + '</p>'
        ret += '<p><b>Spending all time:</b> $' + '{0:.2f}'.format(sum(spending_all_time)) + '</p>'
        return ret

    __mapper_args__ = {
        'polymorphic_identity': 'date_oriented_report_generator',
    }
