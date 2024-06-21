# add function
def add(a, b):
    return a + b

# substract function
def subtract(a, b):
    return a - b

# Divison function
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b