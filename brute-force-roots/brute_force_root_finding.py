from numpy import linspace
from numpy import sin, pi


def main():
    '''Main function to find roots using brute force.'''
    # Define the interval and number of points
    interval_start = 0
    interval_end = 4
    num_points = 1001  # Number of points for evaluation

    # Find roots using brute force
    roots = brute_force_root_finding(g, interval_start, interval_end, num_points)

    if roots:
        # Print the roots
        print(f'Roots of f(x): {roots}')
    else:
        print(f'No roots in [{interval_start}, {interval_end}]')


# Define the functions f(x), g(x), h(x) ... for which we want to find roots
def f(x):
    '''A function example'''
    return x**2 - 4  # f(x) = x^2 - 4

def g(x):
    '''Another function example'''
    return x + 2 * sin(2 * pi * x / 3) - 1


def brute_force_root_finding(f, a, b, n):
    '''
    Find roots of the function within the specified interval using brute force.
    
    Parameters:
    f (callable): The function to find roots for.
    a (float): The start of the interval.
    b (float): The end of the interval.
    n (int): The number of points for evaluation.

    Returns:
    list: A list of roots found within the interval.
    '''

    x_values = linspace(a, b, n)  # Generate equally spaced points in the interval
    y_values = f(x_values)  # Evaluate the function at each point
    roots = []  # Initialize a list to store the roots

    # Iterate through adjacent points
    for i in range(n - 1):
        if y_values[i] * y_values[i + 1] < 0:  # Check for a zero crossing
            # Calculate the root using linear interpolation
            root = x_values[i] - (x_values[i + 1] - x_values[i]) / (y_values[i + 1] - y_values[i]) * y_values[i]
            roots.append(root)
        elif y_values[i] == 0:  # Check if the function is zero at the current point
            root = x_values[i]  # The current point is a root
            roots.append(root)

    return roots


if __name__ == '__main__':
    main()