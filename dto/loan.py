# dto/loan.py

# Pydantic model for loan input validation
from decimal import Decimal
from pydantic import BaseModel

class LoanCreate(BaseModel):
    user_id: int
    loan_amount: Decimal
    interest_rate: Decimal
    term_years: int
    loan_balance: int
    