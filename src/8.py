import random

def mySchoolProject():
    # Generate a random number between 1 and 10
    rand_num = random.randint(1, 10)

    # If the number is even, return "Even"
    if rand_num % 2 == 0:
        return "Even"

    # If the number is odd, return "Odd"
    else:
        return "Odd"
