import random

def account_number(code: str = 'PL'):
    return f"{code}-{random.randint(10000000, 99999999)}"


generate = account_number()

print(generate)