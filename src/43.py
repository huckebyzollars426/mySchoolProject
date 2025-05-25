import random

def generate_random_string(length):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for _ in range(length):
        result.append(random.choice(letters))
    return "".join(result)

print(generate_random_string(10))
