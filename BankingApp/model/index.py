from sqlite3 import OperationalError
from playhouse.postgres_ext import PostgresqlExtDatabase
from model.account import Account
from model.transaction import Transaction
from model.user import User # type: ignore

def create_tables(db: PostgresqlExtDatabase):
    if is_connection_active(db):
        print("Connection is active. Creating tables...")
        tables = [User,Account,Transaction]
        db.create_tables(tables, safe=True)
    else:
        print("Connection is not active. Cannot create tables.")

def is_connection_active(db: PostgresqlExtDatabase) -> bool:
    try:
        # Attempt a simple query to check if the connection is active
        db.execute_sql('SELECT 1')
        return True
    except OperationalError:
        return False