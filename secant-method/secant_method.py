import sys

def main():
    '''Main function to find roots using Secant Method'''

    # Initial guesses for the root
    x0 = 1000
    x1 = x0 - 1
    
    solution, no_iterations = secant(f, x0, x1, eps=1.0e-6)
    
    if no_iterations > 0:  # Solution found
        print('Number of function calls: {:d}'.format(2 + no_iterations))
        print('A solution is: {:f}'.format(solution))
    else:
        print('Solution not found!')

# Example functions
def f(x):
    return x**2 - 4


def secant(f, x0, x1, eps):
    '''
    This function uses the secant method to find the root of a given function.

    Parameters:
    f (callable): The function for which we want to find the root.
    x0 (float): The first initial guess.
    x1 (float): The second initial guess.
    eps (float): The desired accuracy for the root.

    Returns:
    tuple: A tuple containing the root and the number of iterations taken to find the root.
    '''
    # Initialize function values at the initial guesses
    f_x0 = f(x0)
    f_x1 = f(x1)
    # Initialize iteration counter
    iteration_counter = 0

    while abs(f_x1) > eps and iteration_counter < 100:
        try:
            # Compute the new approximation using the secant method
            denominator = (f_x1 - f_x0)/(x1 - x0)
            x = x1 - f_x1/denominator
        except ZeroDivisionError:
            print(f'Error! Zero derivative for x = {x}')
            sys.exit(1)

        # Update values for the next iteration
        x0 = x1
        x1 = x
        f_x0 = f_x1
        f_x1 = f(x1)
        iteration_counter = iteration_counter + 1

    # Check if a solution is found or too many iterations were performed
    if abs(f_x1) > eps:
        iteration_counter = -1
    return x, iteration_counter


if __name__ == '__main__':
    main()