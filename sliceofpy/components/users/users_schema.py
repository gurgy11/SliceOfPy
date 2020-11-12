import datetime as dt
from marshmallow import fields, Schema


class UsersSchema(Schema):

    ''' Table Fields '''

    user_id = fields.Int(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str(required=True)
    address = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    created_at = fields.DateTime(default=dt.datetime.now())

    def __init__(self):
        self.table_name = 'users'
        self.column_names = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
            'username',
            'password',
            'created_at'
        ]
        self.column_types = [
            'INT',
            'VARCHAR(100)',
            'VARCHAR(100)',
            'VARCHAR(255)',
            'VARCHAR(25)',
            'TEXT',
            'VARCHAR(100)',
            'VARCHAR(255)',
            'TIMESTAMP'
        ]
        self.column_definitions = [
            'AUTO_INCREMENT',  # id
            'NOT NULL',  # fname
            'NOT NULL',  # lname
            'NOT NULL',  # email
            '',  # phone
            '',  # address
            'NOT NULL',  # username
            'NOT NULL',  # password
            'NOT NULL DEFAULT CURRENT_TIMESTAMP'
        ]
        self.primary_key = 'id'

    ''' Properties '''

    @property
    def table_name(self):
        return self.table_name

    @property
    def column_names(self):
        return self.column_names

    @property
    def column_types(self):
        return self.column_types

    @property
    def column_definitions(self):
        return self.column_definitions

    @property
    def primary__key(self):
        return self.primary_key
