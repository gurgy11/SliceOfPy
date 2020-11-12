from .db import Database
from .table_template import TableTemplate
from sliceofpy.components.users import UsersTable

def initialize_tables():
    ''' Users Table Setup '''
    users_table = UsersTable()
    if users_table.table_exists() is not True:
        users_table.create_table_if_not_exists()

    ''' Categories Table Setup '''

    ''' Sub-Categories Table Setup '''

    ''' Products Table Setup '''

    ''' Clients Table Setup '''

    ''' Suppliers Table Setup '''

    ''' Warehouses Table Setup '''

    ''' Locations Table Setup '''

    ''' Incoming Orders Table Setup '''

    ''' Outgoing Orders Table Setup '''

    ''' Notifications Table Setup '''
