from fastapi import APIRouter
from dto.auth import UserLoginRequest
from model.auth import authenticate_user

router = APIRouter()

# Route to get all users
@router.post("/auth/", tags=["auth"])
async def auth_user(user_login_request: UserLoginRequest):
          authenticated_user = authenticate_user(user_login_request)  # Call the findAll method from User model
          print(f" this's user record:{authenticated_user}")

          return {"Message:" f"Welcome : {authenticated_user.firstname}!"}
      
      
   