from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    "mydatabase",
    user="sunny",  # Username
    password="sunny",  # Password
    host="localhost",  # Host, can be 'localhost' or remote
    port="5432"  # Port, default is 5432
)