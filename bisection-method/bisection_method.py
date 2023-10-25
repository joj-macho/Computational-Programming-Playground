import math
import numpy as np

def main():
    '''Main function to find and print roots using the bisection method.'''

    print('\nFinding Roots using Bisection Method\n')

    f = lambda x: x**2 - 2  # function f(x)
    x_min = -10  # Lower limit of the root search domain
    x_max = 10  # Upper limit of the root search domain
    interval_width = 0.1  # Width of root separation intervals

    a = x_min  # Initialize the starting point

    while a < x_max:
        # Define the search interval [a, b]
        b = a + interval_width
        # Find the root within the interval [a, b]
        root, iteration_error, iterations = bisect(f, a, b)

        # Check if the root was found successfully (iteration_error == 0) and it's not at the right interval boundary
        if iteration_error == 0 and root != b:
            print(f'Root: {root:.5f} found in interval ({a:.2f}, {b:.2f}) '
                  f'after {iterations} iterations.')
        
        # Shift the left boundary to the right
        a = b


def bisect(f, a, b):
    '''
    Determine a real root x of function f isolated in the interval [a, b] using the bisection method.
    
    Parameters:
        f (function): The function for which the root is to be found.
        a (float): The lower limit of the interval.
        b (float): The upper limit of the interval.

    Returns:
        Tuple: A tuple (root, error_code, iterations) containing:
        - root (float): The estimated root of the function.
        - error_code (int): An error code indicating the outcome:
            0 - Normal execution
            1 - [a, b] does not isolate one root or contains several roots
            2 - Maximum number of iterations exceeded
        - iterations (int): The number of iterations performed to find the root.
    '''
    eps = 1e-6  # Precision/tolerance of the root
    max_iterations = 100  # Maximum number of iterations

    fa = f(a)  # Evaluate the function at a
    if math.fabs(fa) == 0.0:
        return a, 0, 0

    fb = f(b)  # Evaluate the function at b
    if math.fabs(fb) == 0.0:
        return b, 0, 0

    if fa * fb > 0:
        return b, 1, 0  # [a, b] does not contain a root or contains several roots

    for iteration in range(1, max_iterations + 1):
        midpoint = 0.5 * (a + b)  # New approximation
        # midpoint = (a + b) / 2.0
        fx = f(midpoint)

        if fa * fx > 0:
            a = midpoint  # Update the left boundary
        else:
            b = midpoint  # Update the right boundary

        if (b - a) <= eps * math.fabs(midpoint) or math.fabs(fx) <= eps:
            return midpoint, 0, iteration
            
    print('Maximum number of iterations exceeded!')
    return midpoint, 2, max_iterations


if __name__ == '__main__':
    main()
