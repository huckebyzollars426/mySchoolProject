import random

def get_random_code(length):
    alphabet = "1234567890abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in range(length):
        result += random.choice(alphabet)
    return result