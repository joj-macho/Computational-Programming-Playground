import math

def main():
    '''Main function to demonstrate numerical integration using Romberg Integration'''

    print('\nNumerical Integration using Romberg Integration\n')

    # Define the function to be integrated
    f = lambda t: 2 * t * math.exp(-t)
    # Lower and upper limits of the integration interval.
    a = 0; b = 1
    # Number of iterations
    iterations = 5

    # Calculate the numerical integral using Romberg Integration
    numerical = romberg_integration(f, a, b, iterations)

    # Compare the result with the exact integral
    F = lambda t: -2 * (t + 1) * math.exp(-t)
    exact = math.fabs(F(1) - F(0))
    error = abs(exact - numerical)

    print(f'For {iterations} iterations:')
    print(f'Numerical result: {numerical}')
    print(f'Exact result: {exact}')
    print(f'Error: {error:.6e}')


def romberg_integration(f, a, b, iterations):
    '''
    Approximates the definite integral of a function using Romberg Integration.

    Parameters:
        f (function): The function to be integrated.
        a (float): The lower limit of the integration interval.
        b (float): The upper limit of the integration interval.
        iterations (int): The number of extrapolation levels to perform.

    Returns:
        float: The numerical approximation of the integral of the function over the specified interval.
    '''
    # Create a matrix R to store intermediate results
    R = [[0] * (iterations + 1) for _ in range(iterations + 1)]
    # Calculate the initial step size
    h = b - a
    # Compute R[0][0] using the trapezoidal rule for the initial step size
    R[0][0] = 0.5 * h * (f(a) + f(b))

    # Iterate through the specified number of extrapolation levels
    for i in range(1, iterations + 1):
        h /= 2
        # Compute the sum of function values at specific points (odd indexes)
        s = 0

        for k in range(1, 2 ** i, 2):
            s += f(a + k * h)
        # Use the extrapolation formula to calculate R[i][0]
        R[i][0] = 0.5 * R[i - 1][0] + s * h

        # Compute subsequent elements of the row
        for j in range(1, i + 1):
            R[i][j] = R[i][j - 1] + (R[i][j - 1] - R[i - 1][j - 1]) / (4 ** j - 1)

    # The result is in the last column of the last row of the matrix
    return R[iterations][iterations]


if __name__ == '__main__':
    main()
