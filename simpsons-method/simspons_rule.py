import math

def main():
    '''Main function to demonstrate numerical integration using Simpson's Rule'''

    print('\nNumerical Integration using Simpson\'s Rule\n')

    # Define the function to be integrated
    f = lambda t: 2 * t * math.exp(-t)
    # Lower and upper limits of the integration interval.
    a = 0; b = 1
    # Number of subintervals
    n = 20
    if n % 2 != 0:
        raise ValueError('Number of subintervals must be even.')

    # Calculate the numerical integral using Simpson's Rule
    numerical = simpsons_rule(f, 0, 1, n)

    # Compare the result with the exact integral
    F = lambda t: -2 * (t + 1) * math.exp(-t)
    exact = math.fabs(F(1) - F(0))
    error = abs(exact - numerical)

    print(f'For n = {n} subintervals:')
    print(f'Numerical result: {numerical}')
    print(f'Exact result: {exact}')
    print(f'Error: {error:.6e}')


def simpsons_rule(f, a, b, n):
    '''
    Numerically integrate a function using Simpson's Rule.

    Parameters:
        f (function): The function to be integrated.
        a (float): The lower limit of the integration interval.
        b (float): The upper limit of the integration interval.
        n (int): The number of subintervals for Simpson's Rule. It must be an even number.

    Returns:
        float: The numerical approximation of the integral of the function over the specified interval.
    '''
    # Calculate the width of each subinterval
    h = (b - a) / n
    # Initialize the sum to zero
    f_sum = f(a) + f(b)

    # Add up the odd-indexed terms (excluding the first and last)
    for i in range(1, n, 2):
        x = a + i * h
        f_sum += 4 * f(x)

    # Add up the even-indexed terms (excluding the first and last)
    for i in range(2, n - 1, 2):
        x = a + i * h
        f_sum += 2 * f(x)

    return h * f_sum / 3


if __name__ == '__main__':
    main()
