import sys


def main():
    '''Main function to find roots using the Bisection Method'''

    # Define the interval [a, b]
    a = 0
    b = 1000
    
    solution, no_iterations = bisection(f, a, b, eps=1.0e-6)
    
    # Print the number of function calls and the solution
    print('Number of function calls: {:d}'.format(1 + 2*no_iterations))
    print('A solution is: {:f}'.format(solution))

# Example function
def f(x):
    return x**2 - 4


def bisection(f, left_endpoint, right_endpoint, eps):
    '''Find root of the function using the bisection method.'''

    f_left = f(left_endpoint)  # Evaluate function at left endpoint
    if f_left * f(right_endpoint) > 0:
        print("Error! Function does not have opposite signs at interval endpoints!")
        sys.exit(1)

    # Initialize midpoint and iteration counter
    midpoint = (left_endpoint + right_endpoint) / 2.0
    f_mid = f(midpoint)
    iteration_counter = 1

    # Iterate until the function value is within the desired accuracy
    while abs(f_mid) > eps:
        if f_left * f_mid > 0:
            left_endpoint = midpoint
            f_left = f_mid
        else:
            right_endpoint = midpoint
        midpoint = (left_endpoint + right_endpoint) / 2
        f_mid = f(midpoint)
        iteration_counter += 1

    return midpoint, iteration_counter

if __name__ == '__main__':
    main()