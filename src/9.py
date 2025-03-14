
import random

def get_random_string():
    # List of characters to choose from
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    # Length of the random string
    length = 10

    # Start with an empty string
    result = ""

    # Generate a random character from the list of characters and append it to the result
    for i in range(length):
        result += random.choice(chars)

    return result