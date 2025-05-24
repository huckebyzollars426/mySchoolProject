import matplotlib.pyplot as plt

def plot_data(x_values, y_values):
    """
    This function plots two sequences of numbers on one graph.
    
    Parameters:
        x_values (list): The first sequence of x-values.
        y_values (list): The second sequence of y-values corresponding to each x-value in the first sequence.
    """
    plt.plot(x_values, y_values)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Plot of Data')

    # Add a legend
    plt.legend(['Data 1', 'Data 2'])

    # Show plot
    plt.show()

# Example usage:
x = [0, 5, 10]
y = [5, 3.5, 7.5]

plot_data(x, y)
