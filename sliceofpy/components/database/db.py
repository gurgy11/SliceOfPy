from mysql.connector import connect
from sliceofpy.config import db_params as params


class Database():

    ''' Constructor '''

    def __init__(self):
        self.host = params['host']
        self.user = params['user']
        self.password = params['password']
        self.database = params['database']
        self.connection = connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    ''' Returns a cursor for the database connection '''

    def cursor(self):
        return self.connection.cursor()

    ''' Select all rows from a table '''

    def select_all_rows(self, table_name):
        # Build the sql query string
        query = """SELECT * FROM {table_name}""".format(table_name)

        # Get the connection's cursor
        cursor = self.cursor()

        # Execute the query
        cursor.execute(query)

        # Fetch all results from the cursor
        results = cursor.fetchall()

        # Iterate through the results and append to the data array
        data = []
        for res in results:
            data.append(res)

        # Return the array of data
        return data

    ''' Select a table row using its ID '''

    def select_row_by_id(self, table_name, row_id):
        # Build the sql query string
        query = """SELECT * FROM {table_name} WHERE id = {row_id}""".format(
            table_name, row_id)

        # Create a cursor
        cursor = self.cursor()

        # Execute the query
        cursor.execute(query)

        # Fetch cursor results
        results = cursor.fetchall()

        # Store first result in data variable
        data = results[0]

        # Return the single row data
        return data

    ''' Select all rows where condition is met '''

    def select_all_rows_where(self, table_name, column_name, column_value):
        # Build the query string
        query = """SELECT * FROM {table_name} WHERE {column_name} = "{column_value}" """.format(
            table_name, column_name, column_value)

        # Create a cursor
        cursor = self.cursor()

        # Execute cursor
        cursor.execute(query)

        # Fetch cursor results
        results = cursor.fetchall()

        # Store all results in data array
        data = []
        for res in results:
            data.append(res)

        # Return results and there data
        return data

    ''' Inserts a new row into a database table '''

    def insert_row(self, table_name, columns, values):
        ''' Build SQL query string '''
        query = """INSERT INTO {table_name} (""".format(table_name)

        for col in columns:
            col_str = """{column}""".format(col)

            if columns.index(col) == len(columns) - 1:
                col_str += ") "
            else:
                col_str += ", "

            query += col_str

        query += "VALUES ("

        for val in values:
            val_str = """%s"""

            if values.index(val) == len(values) - 1:
                val_str += """) """
            else:
                val_str += """, """

            query += val_str

        print(query)

        ''' Execute query with values using cursor '''
        cursor = self.cursor()
        cursor.execute(query, values)

        ''' Commit changes to database '''
        conn = self.connection
        conn.commit()

    ''' Updates a table row using its ID '''

    def update_row(self, table_name, columns, values, row_id):
        ''' Construct SQL query string '''
        query = """UPDATE {table_name} SET """.format(table_name)

        for col in columns:
            col_str = """{column} = %s""".format(column=col)

            if columns.index(col) == len(columns) - 1:
                col_str += """ """
            else:
                col_str += """, """

            query += col_str

        query += """WHERE id = {row_id} """.format(row_id=row_id)

        ''' Execute query with values '''
        cursor = self.cursor()
        cursor.execute(query, values)

        ''' Commit database changes '''
        conn = self.connection
        conn.commit()

    ''' Deletes a table row using its ID '''

    def delete_row(self, table_name, row_id):
        # Construct SQL query string
        query = """DELETE FROM {table_name} WHERE id = {row_id}""".format(
            table_name=table_name, row_id=row_id)

        # Execute
        cursor = self.cursor()
        cursor.execute(query)

        # Commit
        conn = self.connection
        conn.commit()

    ''' Checks if a table already exists in the database and returns a bool '''

    def table_exists(self, table_name):
        # Query SQL
        query = """SELECT * FROM information_schema.tables WHERE table_schema = '{database_name}' AND table_name = '{table_name}' """.format(
            self.database, table_name)

        # Execute
        cursor = self.cursor()
        cursor.execute(query)

        # Fetch results
        results = cursor.fetchall()

        # Check if table exists (1 or more results indicates True)
        table_exists = False
        if len(results) > 0:
            table_exists = True
        
        return table_exists

    ''' Creates a table in the database '''

    def create_table(self, table_name, column_names, column_types, column_definitions):
        # Build SQL query string
        query = """CREATE TABLE {table_name} ("""

        # Column SQL strings and expressions
        for col in column_names:
            i = column_names.index(col)

            column_name = column_names[i]
            column_type = column_types[i]
            column_definition = column_definitions[i]

            col_str = """{column_name} {column_type} {column_definition}""".format(column_name=column_name, column_type=column_type,
                                                                                   column_definition=column_definition)

            if column_names.index(col) == len(column_names) - 1:
                col_str += """, PRIMARY KEY(id)) ENGINE=INNODB; """
            else:
                col_str += """, """

            query += col_str

        print(query)

        # Execute SQL query
        cursor = self.cursor()
        try:
            cursor.execute(query)

            conn = self.connection
            conn.commit()

            print('Successfully created the new database table: ' + table_name)
        except Exception as e:
            print(
                'A problem occurred while trying to create the new database table: ' + table_name)
            print('The exception thrown is: ' + e)
    
    ''' Creates a database table only if it does not already exist '''

    def create_table_if_not_exists(self, table_name, column_names, column_types, column_definitions):
        # Check if table already exists
        table_exists = self.table_exists(table_name)
        if table_exists is True:
            print('A problem occurred while trying to create a new table. The table already exists!')
            return False
        else:
            self.create_table(table_name, column_names, column_types, column_definitions)
            return True
