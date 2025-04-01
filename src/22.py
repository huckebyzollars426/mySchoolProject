import random

def generate_random_numbers(min_value: int, max_value: int) -> list:
    """Generate a list of random integers within a specified range."""
    return [random.randint(min_value, max_value) for _ in range(random.randint(5, 10))]

print(generate_random_numbers(-10, 10))
