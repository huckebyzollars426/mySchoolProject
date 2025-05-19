def add_numbers(a, b):
    result = a + b
    return result

def subtract_numbers(a, b):
    result = a - b
    return result

def multiply_numbers(a, b):
    result = a * b
    return result

def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero"
    else:
        result = a / b
        return result
