import math

def main():
    '''Main function to evaluate and print the results of trigonometric functions using different methods.'''
    
    print('\nTrigonometric Function Evaluation\n')

    # Test values for the trigonometric functions
    x_values = [0.2, 0.5, 0.8]

    for x in x_values:
        print(f'Input value: x = {x}\n')

        # Calculate sin(x), cos(x), and arccos(x) using different methods
        result_sin_series = sine(x)
        result_real_sin = math.sin(x)

        result_cos_series = cosine(x)
        result_real_cos = math.cos(x)

        result_arcsin_series = arcsine(x)
        result_real_arcsin = math.asin(x)

        result_arccos_series = arccosine(x)
        result_real_arccos = math.acos(x)

        # Calculate tan(x) using different methods
        result_tan_series = tangent_power_series(x)
        result_real_tan = math.tan(x)
        result_tan_cf = tangent_continued_fraction(x)

        # Print results for sin
        print('Real sin(x):', result_real_sin)
        print('sin(x) using power series expansion:', result_sin_series)
        print()

        # Print results for cos
        print('Real cos(x):', result_real_cos)
        print('cos(x) using power series expansion:', result_cos_series)
        print()

        # Print results for arcsin
        print('Real arcsin(x):', result_real_arcsin)
        print('arcsin(x) using power series expansion:', result_arcsin_series)
        print()

        # Print results for arccos
        print('Real arccos(x):', result_real_arccos)
        print('arccos(x) using power series expansion:', result_arccos_series)
        print()

        # Print results for tan
        print('Real tan(x):', result_real_tan)
        print('tan(x) using power series expansion:', result_tan_series)
        print('tan(x) using continued fractions:', result_tan_cf)

        print('\n--------------------------------\n')
    
def sine(x):
    """
    Evaluates sin(x) from its power-series expansion.

    Parameters:
    x (float): The input value.

    Returns:
    float: The sine value sin(x).
    """
    eps = 1e-14
   
    i = 1
    f = t = x
    x2 = x * x
    while math.fabs(t) > eps * math.fabs(f):
        i += 2
        t *= -x2 / ((i - 1) * i)
        f += t

    return f

def cosine(x):
    """
    Evaluates cos(x) from its power-series expansion.

    Parameters:
    x (float): The input value.

    Returns:
    float: The cosine value cos(x).
    """
    eps = 1e-14

    i = 0
    f = t = 1.0
    x2 = x * x

    while math.fabs(t) > eps * math.fabs(f):
        i += 2
        t *= -x2 / ((i - 1) * i)
        f += t

    return f

def arcsine(x):
    """
    Evaluates arcsin(x) from its power-series expansion.

    Parameters:
    x (float): The input value.

    Returns:
    float: The arcsine value arcsin(x).
    """
    eps = 1e-14  # Relative precision
   
    i = 1
    f = t = x
    x2 = x * x
    while math.fabs(t) > eps * math.fabs(f):
        i2 = i * i
        i += 2
        t *= i2 * x2 / ((i - 1) * i)
        f += t

    return f

def arccosine(x):
    """
    Evaluates arccos(x) from its power-series expansion.

    Parameters:
    x (float): The input value.

    Returns:
    float: The arccosine value arccos(x).
    """
    return math.pi/2 - arcsine(x)

def tangent_power_series(x):
    """
    Evaluates tan(x) from its power-series expansion.

    Parameters:
    x (float): The input value.

    Returns:
    float: The tangent value tan(x).
    """
    eps = 1e-14  # Relative precision

    i = 1
    f = t = x
    x2 = x * x
    fact = 1.0

    while math.fabs(t) > eps * math.fabs(f):
        i += 2
        fact *= i * (i - 1)
        t = (x ** i) / fact
        f += t

    return f

def tangent_continued_fraction(x):
    """
    Evaluates tan(x) from its continued fraction representation.

    Parameters:
    x (float): The input value.

    Returns:
    float: The tangent value tan(x).
    """
    eps = 1e-14  # Relative precision

    a = 1.0
    b = -x * x
    pm1 = 0.0
    p = x
    qm1 = 1.0
    q = 1.0
    rm1 = 0.0
    r = x

    while math.fabs(r - rm1) > eps * math.fabs(r):
        pm2 = pm1
        pm1 = p
        qm2 = qm1
        qm1 = q
        rm1 = r
        a += 2.0
        p = a * pm1 + b * pm2
        q = a * qm1 + b * qm2
        r = p / q

    return r

if __name__ == '__main__':
    main()
