class DatabaseConnection:
    _instance = None

    def __new__(cls, database_url):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._database_url = database_url  # Initialize the database connection
            print(f"Database connection established to {database_url}")
        return cls._instance

    def query(self, sql):
        print(f"Executing query on {self._database_url}: {sql}")
        # Execute the query on the database
        # This is a placeholder for actual database interaction logic


if __name__ == "__main__":
    db_conn1 = DatabaseConnection("postgresql://localhost:5432/mydatabase")
    db_conn1.query("SELECT * FROM users")

    db_conn2 = DatabaseConnection("postgresql://localhost:5432/otherdatabase")
    db_conn2.query("SELECT * FROM products")

    print(
        f"db_conn1 is db_conn2: {db_conn1 is db_conn2}"
    )  # True, both are the same instance despite different initialization parameters
