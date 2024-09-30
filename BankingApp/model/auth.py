from fastapi import HTTPException
from model.user import User
from dto.auth import UserLoginRequest
from utils.auth import verify_password
from utils.index import raise_format_error


def authenticate_user(user_login_request: UserLoginRequest) -> User:
    
    try: 
        
        user_record = User.get(User.email == user_login_request.email)
        
        if verify_password(user_login_request.password,user_record.password):
            return user_record
        else:
            raise HTTPException(status_code=401, detail="Invalid password.")
        
    except Exception as e:
        raise raise_format_error(e,"An error occurred during authentication.")
