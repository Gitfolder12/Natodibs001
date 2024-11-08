from peewee import (
    PostgresqlDatabase, Model, DecimalField, AutoField, IntegerField,
    DateField, CharField, fn
)
from datetime import datetime

# Initialize the PostgreSQL database connection
# db = PostgresqlDatabase(
#     "mydatabase",
#     user="sunny",
#     password="sunny",
#     host="localhost",
#     port="5432"
# )

# print('Connecting to database...')

# # Define Transaction model
# class Transaction(Model):
#     amount = DecimalField()  # Field to store the transaction amount
#     type = CharField()       # Field to specify transaction type ('deposit' or 'withdraw')
#     user_id = IntegerField()  # Should match exactly with 'user_id' in the database table
    
#     class Meta:
#         database = db  # Bind this model to the database
#         table_name = 'transaction'  # Specify the existing table name


# # Define LoanCreation model
# class LoanCreation(Model):
#     id = AutoField()
#     user_id = IntegerField()  
#     loan_amount = DecimalField(max_digits=10, decimal_places=2)
#     interest_rate = DecimalField(max_digits=5, decimal_places=2)  # Annual interest rate in percent
#     term_years = IntegerField()  # Loan term in years
#     date_taken = DateField(default=datetime.now)
#     remaining_balance = DecimalField(max_digits=10, decimal_places=2)

#     class Meta:
#         database = db


# def calculate_total_deposit(user_id):
#     """Calculate total deposits for a given user."""
#     try:
#         # Perform the query to calculate total deposits
#         total_deposits = (Transaction
#                           .select(fn.SUM(Transaction.amount))
#                           .where((Transaction.type == 'deposit') & (Transaction.user_id == user_id))
#                           .scalar() or 0.0)
#         return total_deposits
#     except Exception as e:
#         print(f"An error occurred during deposit calculation: {e}")
#         return 0.0


# def grant_loan(user_id, loan_amount, interest_rate, term_years):
#     """Check if loan can be granted and create a loan record if eligible."""
#     total_deposits = calculate_total_deposit(user_id)
#     print(f"Total deposits for user {user_id}: {total_deposits}")

#     if total_deposits >= loan_amount:
#         # Create the loan record in LoanCreation
#         loan = LoanCreation.create(
#             user_id=user_id,
#             loan_amount=loan_amount,
#             interest_rate=interest_rate,
#             term_years=term_years,
#             date_taken=datetime.now(),
#             remaining_balance=loan_amount  # Initialize remaining balance as loan amount
#         )
#         print(f"Loan granted to User ID {user_id} for amount {loan_amount}")
#         return loan
#     else:
#         print(f"Loan request denied for User ID {user_id} - insufficient deposits.")
#         return None


# # Example usage
# if __name__ == "__main__":
#     db.connect(reuse_if_open=True)
    
#     try:
#         user_id = 2
#         loan_amount = 1000
#         interest_rate = 0.05  # 5% annual interest
#         term_years = 2

#         # Attempt to grant a loan
#         loan = grant_loan(user_id, loan_amount, interest_rate, term_years)
        
#     finally:
#         db.close()  # Ensure the database connection is closed at the end


##########################################################################

def amortization_schedule(principal, annual_rate, loan_term_years):
    monthly_rate = annual_rate / 12 / 100
    total_payments = loan_term_years * 12

    # Monthly payment calculation
    monthly_payment = (
        (principal * monthly_rate * (1 + monthly_rate) ** total_payments) /
        ((1 + monthly_rate) ** total_payments - 1)
    )

    balance = principal
    schedule = []

    for i in range(1, total_payments + 1):
        interest = balance * monthly_rate
        principal_paid = monthly_payment - interest
        balance -= principal_paid

        schedule.append({
            "paymentNumber": i,
            "paymentAmount": round(monthly_payment, 2),
            "interestPaid": round(interest, 2),
            "principalPaid": round(principal_paid, 2),
            "remainingBalance": round(balance, 2)
        })

    return schedule

# Example usage
schedule = amortization_schedule(10000, 5, 3)
for payment in schedule:
    print(payment)
