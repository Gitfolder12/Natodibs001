from fastapi import APIRouter, HTTPException
from model.loan import Loan
from dto.loan import LoanCreate

router = APIRouter()

# Route to create a new loan
@router.post("/loans/", response_model=Loan, tags=["loans"])
async def create_loan(loan: LoanCreate):
    try:
        # Attempt to grant a loan by calling the class method
        new_loan = Loan.grant_loan(loan)

        # No need to check for None, as grant_loan will raise an HTTPException on failure
        return new_loan  # Assuming new_loan is already in dictionary format

    except HTTPException as http_exc:
        # Re-raise the HTTPException for errors related to the loan process
        raise http_exc
    except Exception as e:
        # Handle unexpected exceptions
        raise HTTPException(status_code=500, detail=f"Error creating loan: {str(e)}")
