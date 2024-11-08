from peewee import PostgresqlDatabase

# Initialize the PostgreSQL database connection
db = PostgresqlDatabase(
    "mydatabase",
    user="sunny",
    password="sunny",
    host="localhost",
    port="5432"
)
