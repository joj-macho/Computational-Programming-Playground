import math
import numpy as np

def main():
    '''Main function to find and print roots using the False Position Method.'''

    print('\nFinding Roots using False Position Method\n')

    f = lambda x: x**2 - 2  # function f(x)
    x_min = -5  # Lower limit of the root search domain
    x_max = 5  # Upper limit of the root search domain
    h = 0.1  # Width of root separation intervals

    a = x_min
    while a < x_max:
        # Define the search interval [a, b] and find root
        b = a + h
        root, iteration_error, iterations = false_position(f, a, b)

        # Check if the root was found successfully (iteration_error == 0) and it's not at the right interval boundary
        if iteration_error == 0 and root != b:
            print(f'Root: {root:.5f} found in interval ({a:.2f}, {b:.2f}) '
                  f'after {iterations} iterations.')

        # Shift left boundary
        a = b


def false_position(f, a, b):
    '''
    Determines a real root x of function f isolated in the interval [a, b] using the False Position method.
    
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

    fa = f(a)  # Evaluate the function at the left endpoint (a)
    # If fa is already zero, a is a root, return a with error code 0
    if math.fabs(fa) == 0.0:
        return a, 0, 0  

    fb = f(b)  # Evaluate the function at the right endpoint (b)
    # If fb is already zero, b is a root, return b with error code 0
    if math.fabs(fb) == 0.0:
        return b, 0, 0  

    # If fa and fb have the same sign, [a, b] does not contain a root or contains several roots
    if fa * fb > 0:
        return b, 1, 0  

    for iteration in range(1, max_iterations + 1):
        # Calculate the new approximation and evaluate
        x = (a * fb - b * fa) / (fb - fa)
        fx = f(x)

        if fa * fx > 0:
            # Update the difference dx as (new root - a)
            dx = x - a
            a = x
            # Update the function value at the new root
            fa = fx
        else:
            # Update the difference dx as (b - new root)
            dx = b - x
            b = x
            # Update the function value at the new root
            fb = fx

        if (math.fabs(dx) <= eps * math.fabs(x)) or (math.fabs(fx) <= eps):
            return x, 0, iteration

    print('Maximum number of iterations exceeded!')
    return x, 2, max_iterations 



if __name__ == '__main__':
    main()
