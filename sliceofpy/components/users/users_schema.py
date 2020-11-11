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
    password = fields.str(required=True)
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
            'AUTO_INCREMENT', # id
            'NOT NULL', # fname
            'NOT NULL', # lname
            'NOT NULL', # email
            '', # phone
            '', # address
            'NOT NULL', # username
            'NOT NULL', # password
            'NOT NULL DEFAULT CURRENT_TIMESTAMP'
        ]
        self.primary__key = 'id'
