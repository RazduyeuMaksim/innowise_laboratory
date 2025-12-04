import sqlite3

DB_PATH: str = "school.db"
SQL_PATH: str = "queries.sql"

class SQLiteClass:
    def __init__(self, db_path: str, sql_file: str):
        """
        Initialize the SQLiteClass with paths to the database and SQL file.
        """
        self.db_path = db_path
        self.sql_file = sql_file

    def connect_to_database(self) -> sqlite3.Connection:
        """
        Establish a connection to the SQLite database.
        """
        try:
            connection: sqlite3.Connection = sqlite3.connect(self.db_path)
            return connection
        except Exception as e:
            print(f"Failed to connect to the database: {self.db_path}. {e}")
            raise

    def close_connection(self, connection: sqlite3.Connection) -> None:
        """
        Close an active database connection.
        """
        try:
            connection.close()
        except Exception as e:
            print(f"Failed to close connection. {e}")
            raise    

    def execute_scripts(self) -> None:
        """
        Execute the SQL script file against the database.
        """
        connection: sqlite3.Connection = self.connect_to_database()
        
        try:
            with connection:
                with open(self.sql_file) as file:
                    connection.executescript(file.read())
        except Exception as e:
            print(f"Failed to execute file: {self.sql_file}. {e}")
            raise
        finally:
            self.close_connection(connection=connection)
        

def main():
    """
    Entry point of the program.
    """
    sqlite_runner: SQLiteClass = SQLiteClass(DB_PATH, SQL_PATH)
    sqlite_runner.execute_scripts()

if __name__ == "__main__":
    main()
