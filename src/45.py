def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

def main():
    numbers = [10, 20, 30, 40, 50]
    result = calculate_average(numbers)
    print("The average is:", result)

if __name__ == "__main__":
    main()
