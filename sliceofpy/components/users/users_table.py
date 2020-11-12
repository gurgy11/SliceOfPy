'''

Define your database tables that are required on installation here.
These should be tables that are required in order for this application to work.
For example, if you have a login system, you probably want to define a table for users here!

'''

# Local imports
from . import UsersSchema
from sliceofpy.config import db_params as params
from sliceofpy.components.database import Database


''' Users Table '''


class UsersTable():

    # Constructor
    def __init__(self):
        users_schema = UsersSchema()

        self.db = Database()

        self._database_name = params['database']
        self._table_name = users_schema.table_name
        self._column_names = users_schema.column_names
        self._column_types = users_schema.column_types
        self._column_definitions = users_schema.column_definitions
        self._primary_key = users_schema.primary_key

    ''' Checks if the users table exists or not '''

    def table_exists(self):
        table_exists = self.db.table_exists(self.table_name)
        return table_exists

    ''' Initializes the users table in the database '''

    def create_table_if_not_exists(self):
        if self.db.create_table_if_not_exists(
            self.table_name, self.column_names, self.column_types, self.column_definitions):
            return True
        else:
            return False
