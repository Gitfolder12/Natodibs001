from peewee import PostgresqlDatabase, Model, fn
from peewee import (
    Model, CharField,
     FloatField, IntegerField
)

# Initialize the PostgreSQL database connection
db = PostgresqlDatabase(
    "mydatabase",
    user="sunny",
    password="sunny",
    host="localhost",
    port="5432"
)

class Transaction(Model):
    type = CharField()      # Transaction type, e.g., 'deposit'
    amount = FloatField()   # Amount of the transaction
    user = IntegerField()   # User ID for the transaction

    class Meta:
        database = db       # Bind this model to the database
        table_name = 'transaction'  # Specify the existing table name


# Connect to the database
db.connect()

def calculate_total_deposit(user_id):
    """Calculate total deposits for a given user."""
    try:
        # Perform the query to calculate total deposits
        total_deposits = (Transaction
                          .select(fn.SUM(Transaction.amount))
                          .where((Transaction.type == 'deposit') & (Transaction.user == user_id))
                          .scalar() or 0.0)
        return total_deposits
    
    except Exception as e:
        print(f"An error occurred during deposit calculation: {e}")
        return 0.0
    
    finally:
        # Close the database connection
        db.close()

# Calculate and print the sum of deposits for user with ID 2
sum_deposit = calculate_total_deposit(2)
print(f"Total deposits for user 2: {sum_deposit}")
