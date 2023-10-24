import scipy.special

def main():
    '''Main function to evaluate and print the results of orthogonal polynomials.'''

    print('\nEvaluating Orthogonal Polynomials\n')

    x = 0.5  # input value
    n = 3    # order for orthogonal polynomials
    k = 1    # additional parameter for Laguerre polynomials.

    # Evaluate orthogonal polynomials using scipy.special
    chebyshev_special = scipy.special.eval_chebyt(n, x)
    legendre_special = scipy.special.eval_legendre(n, x)
    laguerre_special = scipy.special.eval_laguerre(n, x)
    hermite_special = scipy.special.hermite(n)(x)

    # Evaluate orthogonal polynomials manually
    chebyshev_manual = evaluate_chebyshev(n, x)
    legendre_manual = evaluate_legendre(n, x)
    laguerre_manual = evaluate_laguerre(n, x)
    hermite_manual = evaluate_hermite(n, x)

    # Chebyshev polynomial Results
    print(f'Chebyshev Polynomial of order {n} at x={x}')
    print(f'Chebyshev({n}) using scipy.special: {chebyshev_special}')
    print(f'Chebyshev({n}) evaluated manually: {chebyshev_manual[0]}')
    print(f'Derivative of Chebyshev({n}): {chebyshev_manual[1]}')
    print()

    # Legendre polynomial Results
    print(f'Legendre Polynomial of order {n} at x={x}')
    print(f'Legendre({n}) using scipy.special: {legendre_special}')
    print(f'Legendre({n}) evaluated manually: {legendre_manual[0]}')
    print(f'Derivative of Legendre({n}): {legendre_manual[1]}')
    print()

    # Laguerre polynomial Results
    print(f'Laguerre Polynomial of order {n} at x={x}')
    print(f'Laguerre({n}, {k}) using scipy.special: {laguerre_special}')
    print(f'Laguerre({n}, {k}) evaluated manually: {laguerre_manual[0]}')
    print(f'Derivative of Laguerre({n}, {k}): {laguerre_manual[1]}')
    print()

    # Hermite polynomial Results
    print(f'Hermite Polynomial of order {n} at x={x}')
    print(f'Hermite({n}) using scipy.special: {hermite_special}')
    print(f'Hermite({n}) evaluated manually: {hermite_manual[0]}')
    print(f'Derivative of Hermite({n}): {hermite_manual[1]}')


def evaluate_chebyshev(n, x):
    '''Evaluates the n-th order Chebyshev polynomial and its derivative in x.'''
    if n == 0:
        f = 1.0
        d = 0.0
    else:
        f = x
        fm1 = 1.0
        x2 = 2 * x
        for i in range(2, n + 1):
            fm2 = fm1
            fm1 = f
            f = x2 * fm1 - fm2
        d = n * (x * f - fm1) / (x * x - 1.0) if (x * x - 1.0) else n * n * f / x

    return (f, d)

def evaluate_legendre(n, x):
    '''Evaluates the n-th order Legendre polynomial and its derivative in x.'''
    if n == 0:
        f = 1.0
        d = 0.0
    else:
        f = x
        fm1 = 1.0
        for i in range(2, n + 1):
            fm2 = fm1
            fm1 = f
            f = ((2 * i - 1) * x * fm1 - (i - 1) * fm2) / i
        d = n * (x * f - fm1) / (x * x - 1.0) if (x * x - 1.0) else 0.5 * n * (n + 1) * f / x

    return (f, d)


def evaluate_laguerre(n, x):
    '''Evaluates the n-th order Laguerre polynomial and its derivative in x.'''
    if n == 0:
        f = 1.0
        d = 0.0
    else:
        f = 1.0 - x
        fm1 = 1.0
        for i in range(2, n + 1):
            fm2 = fm1
            fm1 = f
            f = ((2 * i - 1 - x) * fm1 - (i - 1) * fm2) / i
        d = n * (f - fm1) / x if x else -n * f

    return (f, d)


def evaluate_hermite(n, x):
    '''Evaluates the n-th order Hermite polynomial and its derivative in x.'''

    if n == 0:
        f = 1.0
        d = 0.0
    else:
        f = 2 * x
        fm1 = 1.0
        x2 = 2 * x
        for i in range(2, n + 1):
            fm2 = fm1
            fm1 = f
            f = x2 * fm1 - 2 * (i - 1) * fm2
        d = 2 * n * fm1

    return (f, d)


if __name__ == '__main__':
    main()

