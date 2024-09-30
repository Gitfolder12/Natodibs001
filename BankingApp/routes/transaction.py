from fastapi import APIRouter, HTTPException
from model.transaction import Transaction
from dto.transaction import TransactionCreate

router = APIRouter()

# Route to get all Transaction
@router.get("/transactions/", tags=["transactions"])
async def get_transactions():
    transaction = Transaction.findAll()  # Call the findAll method from User model
    return transaction

# Route to get all Transaction
@router.get("/transactions/{id}", tags=["transactions"])
async def get_transaction(id: str):
    id = int(id)
    transaction = Transaction.findOne(id)  # Call the findAll method from User model
    return transaction

# Route to create a new transaction
@router.post("/transactions/", tags=["transactions"])
async def create_transaction(transaction: TransactionCreate):
    try:
        new_transaction = Transaction.create_transaction(transaction)
        return new_transaction
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating transaction: {str(e)}")

