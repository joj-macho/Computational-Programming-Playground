import math
import numpy as np

def main():
    '''Main function to find and print roots using the Secant Method.'''
    
    print('\nFinding Roots using Secant Method\n')

    f = lambda x: x**2 - 2  # function f(x)
    x_min = -5  # Lower limit of the root search domain
    x_max = 5  # Upper limit of the root search domain
    h = 0.1  # Width of root separation intervals

    a = x_min
    while a < x_max:
        # Define the search interval [a, b] and find root
        b = a + h  # Search interval [a, b]
        x = a + 0.5 * h  # Initial approximation
        root, iteration_error, iterations = secant(f, a, b, x)

        # Check if the root was found successfully (iteration_error == 0) and it's not at the right interval boundary
        if iteration_error == 0 and root != b:
            print(f'Root: {root:.5f} found in interval ({a:.2f}, {b:.2f}) '
                  f'after {iterations} iterations.')

        # Shift left boundary
        a = b


def secant(f, a, b, x):
    '''
    Determines a real root x of function f isolated in the interval [a, b] using the Secant method.
    
    Parameters:
        f (function): The function for which the root is to be found.
        a (float): The lower limit of the interval.
        b (float): The upper limit of the interval.
        x (float): An initial approximation of the root.

    Returns:
        Tuple: A tuple (root, error_code, iterations) containing:
        - root (float): The estimated root of the function.
        - error_code (int): An error code indicating the outcome:
            0 - Normal execution
            1 - Interval does not contain a root
            2 - Maximum number of iterations exceeded
        - iterations (int): The number of iterations performed to find the root.
    '''
    eps = 1e-10  # Precision/tolerance of the root
    max_iterations = 1000  # Maximum number of iterations

    # Initialize variables x0 and f0 with the initial approximation x and the value of the function f(x) at that point.
    x0 = x
    f0 = f(x0)
    # Calculate the first approximation of the root
    x = x0 - f0

    for iteration in range(1, max_iterations + 1):
        fx = f(x)  # Calculate the function value f(x) at the current approximation x.
        df = (fx - f0) / (x - x0)  # Calculate approximate derivative based on the change in function values and changes in the approximation x.
        # Update x0 and f0 with the current values of x and f(x)
        x0 = x
        f0 = fx

        # Calculate the root correction dx and update the current approximation x
        dx = -fx / df if math.fabs(df) > eps else -fx
        x += dx

        # Check if the new approximation x is outside the interval [a, b]
        if x < a or x > b:
            return x, 1, 0
        # Check for convergence of the root
        if math.fabs(dx) <= eps * math.fabs(x):
            return x, 0, iteration  # Check convergence

    print('Secant: Maximum number of iterations exceeded!')
    return x, 2, max_iterations


if __name__ == '__main__':
    main()
