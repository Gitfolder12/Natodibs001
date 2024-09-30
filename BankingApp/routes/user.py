from fastapi import APIRouter
from model.user import User
from dto.user import UserCreate

router = APIRouter()

# Route to get all users
@router.get("/users/", tags=["users"])
async def get_users():
    users = User.findAll()  # Call the findAll method from User model
    return users


# Route to create a new user (POST)
@router.post("/users/", tags=["users"])
async def create_user(user: UserCreate):
    # Create a new user and save to the database
     new_user = User.create_user(user)
     return new_user