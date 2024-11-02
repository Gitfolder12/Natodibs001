# dtos/users.py

# Pydantic model for user input validation
from pydantic import BaseModel

class UserCreate(BaseModel):
    firstname: str
    lastname: str
    phone: int
    email: str
      