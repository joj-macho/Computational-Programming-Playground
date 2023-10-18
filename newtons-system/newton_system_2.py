import numpy as np

def main():
    '''Main function to solve a nonlinear system using Newton's method.'''
    
    # Expected values and tolerance
    expected = np.array([1, 0])
    tol = 1e-4

    # Solve the system using Newton's method
    x, n, iteration_results = newton_system(F, eps=0.0001)

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


def calculate_jacobian(F, x, eps=1e-6):
    '''Calculate the Jacobian matrix of the system using finite differences.'''
    n = len(x)  # dimension of the system
    J = np.zeros((n, n))  # Empty matrix to store J
    F_value = F(x)  # Calculate f value at current point x

    # Iterate over each dimension of the system:
    for i in range(n):
        # small perturbation in the i-th dimension using eps.
        x_temp = np.array(x, dtype=complex)
        x_temp[i] = x[i] + eps * 1j
        # Compute the function values at the perturbed point.
        F_temp = F(x_temp)
        # Approximate the derivative using finite differences
        J[:, i] = np.imag(F_temp) / eps
    return J


def newton_system(F, eps):
    '''
    Solve a nonlinear system F=0 using Newton's method.

    Parameters:
        F (callable): System of nonlinear equations.
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

    # Iterate until the norm of F is within the desired accuracy
    while abs(F_norm) > eps and iteration_counter < 100:
        J = calculate_jacobian(F, x)
        delta = np.linalg.solve(J, -F_value)
        x = x + delta
        F_value = F(x)
        F_norm = np.linalg.norm(F_value, ord=2)
        iteration_counter += 1
        iteration_results.append((x, F_value))

    # Check if a solution is found or too many iterations were performed
    if abs(F_norm) > eps:
        iteration_counter = -1

    return x, iteration_counter, iteration_results

if __name__ == '__main__':
    main()
