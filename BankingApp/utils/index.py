import random

from fastapi import HTTPException
from pydantic import ValidationError

def generate_account_number():
    return random.randint(10000000, 99999999)


def raise_format_error(e: ValidationError, title: str = '') -> str:
    # Join all error messages into a single string
    if isinstance(e, ValidationError):
        errors = e.errors()  # Get all validation errors
        messages = [f"{error['loc'][0]}: {error['msg']}" for error in errors]
        # Handle validation errors
        formatted_message = ", ".join(messages)
        raise HTTPException(
            status_code=400, detail=f"Validation errors: {formatted_message}"
        )
    else:
        # Handle generic exceptions
        raise HTTPException(status_code=400, detail=f"{title} Error: {str(e)}")
