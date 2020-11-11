import datetime as dt
from marshmallow import fields, Schema


class TableTemplate(Schema):

    def __init__(self):
        self._id = fields.Int(required=True)
        self._created_at = fields.DateTime(default=dt.datetime.now())

    ''' Properties '''

    @property
    def id(self):
        return self._id

    @property
    def created_at(self):
        return self._created_at

    ''' Setters '''

    @id.setter
    def id(self, _id):
        self._id = _id

    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at

    ''' Class Methods '''

    def to_dict(self):
        table_dict = {
            'id': self._id,
            'created_at': self._created_at
        }

        return table_dict

