from fastapi import HTTPException
from peewee import Model, IntegerField, DateField, AutoField, DecimalField, fn
from connection.index import db
from datetime import datetime
from dto.loan import LoanCreate
from model.transaction import Transaction


class Loan(Model):
    id = AutoField()
    user = IntegerField()
    loan_amount = DecimalField(max_digits=10, decimal_places=2)
    interest_rate = DecimalField(max_digits=5, decimal_places=2)  
    term_years = IntegerField()  
    date_taken = DateField(default=datetime.now)
    loan_balance = DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        database = db

    @classmethod
    def find_all(cls) -> list:
        """Retrieve all loans."""
        return [loan.__data__ for loan in cls.select()]

    @classmethod
    def grant_loan(cls, loan_data: LoanCreate) -> "Loan": 
        """
        Attempts to create a loan for a user if their total deposits meet the loan amount requirement.
        """
        try:
            # Calculate the total deposits for the user
            total_deposits = (Transaction
                              .select(fn.SUM(Transaction.amount))
                              .where((Transaction.type == 'deposit') &  (Transaction.user_id == loan_data.user))  
                              .scalar() or 0.0)

            # # Debugging output for total deposits
            print(f"Total deposits for user {loan_data.user}: {total_deposits}")
            
            # Check if deposits meet or exceed the loan amount
            if total_deposits >= loan_data.loan_amount:
                # Create the loan record
                loan_dict = loan_data.model_dump()
                loan_dict['loan_balance'] = loan_data.loan_amount
                loan_instance = cls.create(**loan_dict)
                return loan_instance.__data__
            else:
                raise HTTPException(status_code=404, detail="Loan request denied for User: insufficient deposits") 
        except Exception as e:
            print(f"Error while granting loan: {e}")
            raise HTTPException(status_code=500, detail="Internal server error while processing loan request.")
