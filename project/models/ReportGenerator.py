from project import db
from flask import make_response
from io import StringIO
import csv
import json


class ReportGenerator(db.Model):
    # Only superclass gets tablename
    __tablename__ = 'report_generator'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(80), nullable=False)
    # Field for distinguishing between subclasses
    type = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, filename):
        self.filename = filename

    # Setup for single table polymorphic stuff in sqlalchemy
    # https://docs.sqlalchemy.org/en/latest/orm/inheritance.html
    __mapper_args__ = {
        'polymorphic_identity': 'report_generator',
        'polymorphic_on': type
    }


class CSVReportGenerator(ReportGenerator):
    def __init__(self, filename):
        super(CSVReportGenerator, self).__init__(filename)

    def generate_report(self, instances):
        # Code for generating csv
        # https://stackoverflow.com/questions/11914472/
        # https://stackoverflow.com/questions/26997679/
        sio = StringIO()
        writer = csv.writer(sio)
        # Float formatting
        # Make nested list for writerows
        instances = [[i.__str__(), '{0:.2f}'.format(i.amount), i.account.name, i.date] for i in instances]
        writer.writerows(instances)
        output = make_response(sio.getvalue())
        output.headers['Content-Disposition'] = 'attachment; filename=' + self.filename + '.csv'
        output.headers['Content-type'] = 'text/csv'
        return output

    __mapper_args__ = {
        'polymorphic_identity': 'csv_report_generator',
    }


class JSONReportGenerator(ReportGenerator):
    def __init__(self, filename):
        super(JSONReportGenerator, self).__init__(filename)

    def generate_report(self, instances):
        # Code for generating json
        # https://stackoverflow.com/questions/51981089/
        sio = StringIO()
        # Float formatting
        # Make nested list for writerows
        # TODO:
        # Utilize spending instance IDs for better JSON formatting
        instances = [{i.__str__(): ['{0:.2f}'.format(i.amount), i.account.name, str(i.date)]} for i in instances]
        json.dump(instances, sio)
        output = make_response(sio.getvalue())
        output.headers['Content-Disposition'] = 'attachment; filename=' + self.filename + '.json'
        output.headers['Content-type'] = 'application/json'
        return output

    __mapper_args__ = {
        'polymorphic_identity': 'json_report_generator',
    }