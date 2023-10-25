import math

def main():
    '''Main function to demonstrate numerical integration using the Composite Midpoint Method'''

    print('\nNumerical Integration using the Composite Midpoint Method.\n')

    # Define the function to be integrated
    f = lambda t: 2 * t * math.exp(-t)
    # Lower and upper limits of the integration interval.
    a = 0; b = 1
    # Number of subintervals
    n = 20

    # Calculate the numerical integral using the midpoint method
    numerical_solution = midpoint(f, a, b, n)

    # Compare the result with the exact integral
    F = lambda t: -2 * (t + 1) * math.exp(-t)
    exact_solution = math.fabs(F(1) - F(0))
    error = abs(exact_solution - numerical_solution)
    
    print(f'For n = {n} subintervals:')
    print(f'Numerical result: {numerical_solution}')
    print(f'Exact result: {exact_solution}')
    print(f'Error: {error:.6e}')


def midpoint(f, a, b, n):
    '''
    Numerically integrate a function using the Composite Midpoint Method.

    Parameters:
        f (function): The function to be integrated.
        a (float): The lower limit of the integration interval.
        b (float): The upper limit of the integration interval.
        n (int): The number of subintervals for the Composite Midpoint Method.

    Returns:
        float: The numerical approximation of the integral of the function over the specified interval.
    '''
    # Calculate the width of each subinterval
    h = (b-a)/n
    # Initialize the sum to zero
    f_sum = 0

    # Iterate through the subintervals
    for i in range(0, n, 1):
        x = (a + h/2.0) + i*h
        f_sum = f_sum + f(x)

    return h*f_sum


if __name__ == '__main__':
    main()
