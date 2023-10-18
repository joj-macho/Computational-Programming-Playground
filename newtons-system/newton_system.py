import numpy as np

def main():
    '''Main function to solve a nonlinear system using Newton's method.'''
    
    # Expected values and tolerance
    expected = np.array([1, 0])
    tol = 1e-4

    # Solve the system using Newton's method
    x, n, iteration_results = newton_system(F, J, eps=0.0001)

    # Solution and iteration information
    print(f'Solution:\n{x}')
    print(f'\nNumber of iterations: {n}')
    
    # Results for each iteration
    print('\nResults for each iteration:')
    for i, result in enumerate(iteration_results):
        print(f'Iteration {i+1}: {result}')

    # Calculate the error and check for tolerance
    error_norm = np.linalg.norm(expected - x, ord=2)
    print(f'\nNorm of error: {error_norm}')
    if error_norm < tol:
        print('Error within tolerance.')
    else:
        print('Error exceeds tolerance.')


def F(x):
    '''System of nonlinear equations.'''
    return np.array(
        [x[0]**2 - x[1] + x[0]*np.cos(np.pi*x[0]),
         x[0]*x[1] + np.exp(-x[1]) - x[0]**(-1.)])


def J(x):
    '''Jacobian matrix of the system.'''
    return np.array(
        [[2*x[0] + np.cos(np.pi*x[0]) - np.pi*x[0]*np.sin(np.pi*x[0]), -1],
         [x[1] + x[0]**(-2.), x[0] - np.exp(-x[1])]])


def newton_system(F, J, eps):
    '''
    Solve a nonlinear system F=0 using Newton's method.

    Parameters:
        F (callable): System of nonlinear equations.
        J (callable): Jacobian matrix of the system.
        eps (float): Desired accuracy.

    Returns:
        tuple: A tuple containing the solution, the number of iterations, and results for each iteration.
    '''

    # Initialize variables
    x = np.array([2, -1])  # Initial guess
    F_value = F(x)
    F_norm = np.linalg.norm(F_value, ord=2)  # Calculate the l2 norm of the function values
    iteration_counter = 0
    iteration_results = []

    # Iterate until the norm of F is within the desired accuracy or maximum iterations reached
    while abs(F_norm) > eps and iteration_counter < 100:
        delta = np.linalg.solve(J(x), -F_value)  # Compute the update using the Jacobian and function values
        x = x + delta  # Update the approximation
        F_value = F(x)  # Recompute the function values
        F_norm = np.linalg.norm(F_value, ord=2)  # Compute the l2 norm of the updated function values
        iteration_counter += 1
        iteration_results.append((x, F_value))

    # Check if a solution is found or too many iterations were performed
    if abs(F_norm) > eps:
        iteration_counter = -1

    return x, iteration_counter, iteration_results


if __name__ == '__main__':
    main()
