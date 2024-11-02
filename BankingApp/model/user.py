from http.client import HTTPException
from fastapi import HTTPException
from typing import List
from peewee import Model, CharField, IntegerField, AutoField
from connection.index import db
from dto.user import UserCreate
from dto.account import AccountCreate
from utils.index import generate_account_number, raise_format_error
from utils.auth import hash_password ,validate_password
from model.account import Account


class User(Model):
    id = AutoField()
    firstname = CharField()
    lastname = CharField()
    phone = IntegerField()
    email = CharField(unique=True)
    password = CharField()
    age = IntegerField()
    
    
    
    class Meta:
        database = db

    @classmethod
    def findAll(cls) -> List["User"]:
        return [user.__data__ for user in cls.select()]

    @classmethod
    def create_user(cls, user: UserCreate) -> "User":
        
        hash_pass = hash_password(user.password) # covert password to hash value
        
        if not validate_password(user.password):
           raise HTTPException(status_code=400,
                                            detail="Password must contain at least 8 characters, "
                                                "including at least one lowercase letter, "
                                                "one uppercase letter, one digit, and one special character."
                                            )
        with db.atomic():
                try:

                    user_dict = user.model_dump()
                    
                    user_dict['password'] = hash_pass  #pdate password with hash value in model dump 
                    
                    new_user = cls.create(**user_dict)
                    
                    account_number = generate_account_number()
                
                    new_account = {"user": new_user.id, "number": account_number}
                    
                    account_create = AccountCreate(**new_account)

                    user_account = Account.create_account(account_create)
                    
                    create = {"new_user": new_user.__data__,"user_account": user_account
                              }
                    
                    return create
                except Exception as e:
                       raise_format_error(e,'creating user')
                    
                
              
    @classmethod
    def findOne(cls, id: int) -> "User":
        user = cls.get_or_none(cls.id == id)  # Get user by ID
        print(user)
        if user:
            return user  # Return the field data only

        return None
    
    