import sys

def main():
    '''Main function to find roots using Newton-Rhapson Method'''

    solution, no_iterations = newton(f, dfdx, x=1000, eps=1.0e-6)
    
    if no_iterations > 0:  # Solution found
        print('Number of function calls: {:d}'.format(1+2*no_iterations))
        print('A solution is: {:f}'.format(solution))
    else:
        print('Solution not found!')


# Example functions and its derivative
def f(x):
    return x**2 - 4
    
def dfdx(x):
    return 2*x
    

def newton(f, dfdx, x, eps):
    '''    
    This function uses the Newton-Raphson method to find the root of a given function.

    Parameters:
    f (callable): The function for which we want to find the root.
    dfdx (callable): The derivative of the function.
    x (float): The initial guess for the root.
    eps (float): The desired accuracy for the root.

    Returns:
    tuple: A tuple containing the root and the number of iterations taken to find the root.
    '''
    f_value = f(x)  # Evaluate the function at the initial guess
    iteration_counter = 0  # Initialize iteration counter

    # Iterate until the function value is within the desired accuracy or the maximum number of iterations is reached
    while abs(f_value) > eps and iteration_counter < 100:
        try:
            # Update x using the Newton-Raphson formula to approach the root
            x = x - f_value/dfdx(x)
        except ZeroDivisionError:
            print(f'Error! Zero derivative for x = {x}')
            sys.exit(1)

        # Evaluate the function at the updated x and increment the iteration counter
        f_value = f(x)
        iteration_counter = iteration_counter + 1

    # Check if a solution is found or too many iterations were performed
    if abs(f_value) > eps:
        iteration_counter = -1

    return x, iteration_counter

if __name__ == '__main__':
    main()

