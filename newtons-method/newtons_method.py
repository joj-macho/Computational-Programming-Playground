import math
import numpy as np

def main():
    '''Main function to find and print roots using the Newton-Raphson Method (Numerical Derivative).'''

    print('\nFinding Roots using Newton-Raphson Method with Numerical Derivative\n')

    f = lambda x: x**2 - 2  # function f(x)
    x_min = -10  # Lower limit of the root search domain
    x_max = 10  # Upper limit of the root search domain
    h = 0.1  # Width of root separation intervals

    a = x_min
    while a < x_max:
        # Define the search interval [a, b] and find root
        b = a + h  # Search interval [a, b]
        x = (a + b) / 2  # Initial approximation
        root, iteration_error, iterations = newton_raphson(f, a, b, x)

        # Check if the root was found successfully (iteration_error == 0) and it's not at the right interval boundary
        if iteration_error == 0 and root != b:
            print(f'Root: {root:.5f} found in interval ({a:.2f}, {b:.2f}) '
                  f'after {iterations} iterations.')

        # Shift left boundary
        a = b


def newton_raphson(f, a, b, x):
    '''
    Determines a real root x of function f isolated in interval [a, b] using the Newton-Raphson method with numerical derivative.
    
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
    max_iterations = 100  # Maximum number of iterations

    for iteration in range(1, max_iterations + 1):
        fx = f(x)  # Evaluate the function at the current approximation x
        dx = eps * math.fabs(x) if x else eps  # Determine the derivation step for numerical differentiation
        df = (f(x + dx) - fx) / dx  # Calculate the numerical derivative of f

        if math.fabs(df) < eps:
            dx = -fx  # Avoid division by very small df
        else:
            dx = -fx / df  # Determine the root correction

        x += dx  # Update the current approximation with the root correction

        # If the root is outside the interval [a, b], return error code 1
        if not a <= x <= b:
            return x, 1, 0


        # If the root is converged, return the root and success code (0)
        if math.fabs(dx) <= eps * math.fabs(x):
            return x, 0, iteration

    print('Maximum number of iterations exceeded!')
    return x, 2, max_iterations

if __name__ == '__main__':
    main()
