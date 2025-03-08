import random

def mySchoolProject():
    # Generate a random number between 1 and 10
    rand_num = random.randint(1, 10)
    if rand_num % 2 == 0:
        return "even"
    else:
        return "odd"
