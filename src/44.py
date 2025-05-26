def calculate_average(numbers):
    if not numbers:
        return None
    
    total = sum(numbers)
    average = total / len(numbers)
    return round(average, 2)

numbers = [10.5, 20.3, 30.7]
result = calculate_average(numbers)
print(result)  # Output: 21.38
