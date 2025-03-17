import random
import datetime
def get_random_number(n):
    return random.randint(0, n)
def get_current_time():
    return datetime.datetime.now().strftime("%H:%M")
def get_current_date():
    return datetime.datetime.now().strftime("%d/%m/%Y")