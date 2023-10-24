import math

def main():
    ''' Main function to evaluate and print the results of the exponential function using different methods.'''
    
    print('\nExponential Function Evaluation\n')

    # Test values for the exponential function
    x_values = [0.5, 1.0, -0.5]
    
    for x in x_values:
        print(f'Input value: x = {x}\n')

        # Calculate exp(x) using different methods
        result_exp_series = exponential_series(x)
        result_exp_cf = exponential_continued_fraction(x)
        result_real_exp = math.exp(x)  # Calculate the real exponential value

        # Print results for each method and the real exponential value
        print('Real exp(x):', result_real_exp)
        print('exp(x) using power series expansion:', result_exp_series)
        print('exp(x) using continued fraction representation:', result_exp_cf)

        print('\n--------------------------------\n')


def exponential_series(x):
    '''Evaluates exp(x) from its power-series expansion.'''

    relative_precision = 1e-14
    iteration = 0
    current_term = total = 1.0
    abs_x = math.fabs(x)

    while current_term > relative_precision * math.fabs(total):
        iteration += 1
        current_term *= abs_x / iteration
        total += current_term

    return total if (x >= 0.0) else 1.0 / total


def exponential_continued_fraction(x):
    '''Evaluates exp(x) from its continued fraction representation.'''

    # Initialize variables for the continued fraction calculation
    relative_precision = 1e-14
    a = 1.0  # numerator coefficient in the continued fraction
    b = x  # denominator coefficient in the continued fraction
    pm1 = 1.0  # term p(m-1) in the continued fraction
    p = 1.0 + x  # current term in the continued fraction, initialized as 1.0 + x
    qm1 = 1.0  # term q(m-1) in the continued fraction
    q = 1.0  # current term in the continued fraction and starts as 1.0.
    rm1 = 1.0  # previous convergent value
    r = p / q  # current convergent value
    i = 1  # iteration counter, starting at 1.

    # Continue calculating the continued fraction until the desired precision is achieved
    while (math.fabs(r - rm1) > relative_precision * math.fabs(r)):
        i += 1
        # Update numerator and denominator of the continued fraction
        pm2 = pm1
        pm1 = p
        qm2 = qm1
        qm1 = q
        rm1 = r
        a = (i if i % 2 else 2.0)
        b = -b
        p = a * pm1 + b * pm2
        q = a * qm1 + b * qm2
        r = (p / q if q else 9e99)  # New convergent value

    return r


if __name__ == '__main__':
    main()
