import math

def calculate_volume(length, width, height):
    """
    Calculate the volume of a rectangular prism.
    
    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    
    Returns:
        float: The volume of the rectangular prism.
    """
    return length * width * height

# Example usage
length = 5.0
width = 3.0
height = 4.0
volume = calculate_volume(length, width, height)
print(f"The volume is {volume:.2f} cubic units.")
