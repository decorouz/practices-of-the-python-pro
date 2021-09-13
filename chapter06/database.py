# Persistence Layer for Bark
import sqlite3


class DatabaseManager:
    """The database module provides most of what you need to manage book data, including the following:
        1. Creating a table
        2. Adding or deleting a record
        3. Listing the records in a table
        4. Selecting and sorting records from a table based on some criteria
        Counting the number of records in a table
    """

    # Database connection and the ability to execute arbitrary statments on the connection
    def __init__(self, database_filename):
        self.connection = sqlite3.connect(database_filename)

    def _del__(self):
        self.connection.close()

    def _execute(self, statement, values=None):
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(statement, values or [])
            return cursor
    # Creating Tables
    # Determine the column names for the table
    # Determine the data type of each column
    # Constrcut the right SQL statement to create a table with those columns

    def create_table(self, table_name, columns):
        columns_with_types = [
            f"{column_name} {data_type}" for column_name, data_type in columns.items()
        ]
        self._execute(
            f"""
            CREATE TABLE IF NOT EXISTS {table_name}
            ({", ".join(columns_with_types)});
            """
        )

    def drop_table(self, table_name):
        self._execute(f"DROP TABLE {table_name}")

    # Adding Records

    def add(self, table_name, data):
        placeholders = ", ".join("?" * len(data))
        column_names = ", ".join(data.keys())
        column_values = tuple(data.values())

        self._execute(
            f"""
            INSERT INTO {table_name}
            ({column_names})
            VALUES ({placeholders})
            """,
            column_values
        )
    # Deleting Records

    def delete(self, table_name, criteria):
        placeholders = [f"{column} = ?" for column in criteria.keys()]
        delete_criteria = " AND ".join(placeholders)

        self._execute(
            f"""
            DELETE FROM {table_name}
            WHERE {delete_criteria}
            """,
            tuple(criteria.values())
        )
    # Selecting and Sorting Records

    def select(self, table_name, criteria=None, order_by=None):
        criteria = criteria or {}

        query = f"SELECT * FROM {table_name}"
        if criteria:
            placeholders = [f"{column} = ? " for column in criteria.keys()]
            select_criteria = " AND ".join(placeholders)
            query += f" WHERE {select_criteria}"

        if order_by:
            query += f" ORDER BY {order_by}"

        return self._execute(
            query,
            tuple(criteria.values())
        )
