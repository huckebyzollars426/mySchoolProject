def calculate_average_grades(scores):
    """
    Calculate the average grade of students based on their scores.
    
    Args:
        scores (list): A list of integers representing student scores.
        
    Returns:
        float: The average grade of the students.
    """
    if not scores:
        return 0.0
    
    total = sum(scores)
    average = total / len(scores)
    return average

# Example usage
scores = [95, 88, 76]
average_grade = calculate_average_grades(scores)
print(f"The average grade is: {average_grade}")
