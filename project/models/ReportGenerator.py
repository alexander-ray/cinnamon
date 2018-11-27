from project import db
from flask import make_response
from io import StringIO
import csv
import json
from abc import abstractmethod, ABCMeta
from sqlalchemy.ext.hybrid import hybrid_property


class ReportGenerator(db.Model):
    # Only superclass gets tablename
    __tablename__ = 'report_generator'
    __metaclass__ = ABCMeta

    _id = db.Column(db.Integer, primary_key=True)
    _default_filename = db.Column(db.String(80), nullable=False)

    # Field for distinguishing between subclasses
    _type = db.Column(db.String(80))
    _user_id = db.Column(db.Integer, db.ForeignKey('user._id'))

    def __init__(self, filename):
        self._default_filename = filename

    @abstractmethod
    def generate_report(self, instances, include_description):
        """
        Abstract method to generate report, must be implemented by subclasses

        :param instances: List of spending instance objects
        :param include_description: Boolean value to determine whether or not to include a description
        """
        pass

    @hybrid_property
    def default_filename(self):
        """
        Getter for default filename of report generator

        :return: Default filename
        """
        return self._default_filename

    @default_filename.setter
    def default_filename(self, filename):
        """
        Setter for default filename of report generator

        :param filename: New default filename
        """
        self._default_filename = filename

    # Setup for single table polymorphic stuff in sqlalchemy
    # https://docs.sqlalchemy.org/en/latest/orm/inheritance.html
    __mapper_args__ = {
        'polymorphic_identity': 'report_generator',
        'polymorphic_on': _type
    }


class CSVReportGenerator(ReportGenerator):
    def __init__(self, filename):
        super(CSVReportGenerator, self).__init__(filename)

    def generate_report(self, instances, include_description):
        # Code for generating csv
        # https://stackoverflow.com/questions/11914472/
        # https://stackoverflow.com/questions/26997679/
        """
        CSV report generator, using Python's CSV module

        :param instances: List of spending instance objects
        :param include_description: Toggle for including description
        :return: Flask response object
        """
        sio = StringIO()
        writer = csv.writer(sio)
        # Make nested list for writerows
        if include_description:
            instances = [[i.id, i.__str__(), '{0:.2f}'.format(i.amount),
                          i.account.name, i.date, i.description] for i in instances]
        else:
            instances = [[i.id, i.__str__(), '{0:.2f}'.format(i.amount),
                          i.account.name, i.date] for i in instances]

        writer.writerows(instances)
        output = make_response(sio.getvalue())
        output.headers['Content-Disposition'] = 'attachment; filename=' + self.default_filename + '.csv'
        output.headers['Content-type'] = 'text/csv'
        return output

    __mapper_args__ = {
        'polymorphic_identity': 'csv_report_generator',
    }


class JSONReportGenerator(ReportGenerator):
    def __init__(self, filename):
        super(JSONReportGenerator, self).__init__(filename)

    def generate_report(self, instances, include_description):
        # Code for generating json
        # https://stackoverflow.com/questions/51981089/
        """
        JSON report generator, using Python's JSON module

        :param instances: List of spending instance objects
        :param include_description: Toggle for including description
        :return: Flask reponse object
        """
        sio = StringIO()

        # Float formatting
        # Make nested list for writerows
        if include_description:
            instances = [{i.id: [i.__str__(), '{0:.2f}'.format(i.amount),
                                 i.account.name, str(i.date), i.description]} for i in instances]
        else:
            instances = [{i.id: [i.__str__(), '{0:.2f}'.format(i.amount),
                                 i.account.name, str(i.date)]} for i in instances]
        json.dump(instances, sio)
        output = make_response(sio.getvalue())
        output.headers['Content-Disposition'] = 'attachment; filename=' + self.default_filename + '.json'
        output.headers['Content-type'] = 'application/json'
        return output

    __mapper_args__ = {
        'polymorphic_identity': 'json_report_generator',
    }