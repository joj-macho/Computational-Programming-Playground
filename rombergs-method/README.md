# Numerical Integration using Romberg Integration

## Description

Romberg Integration is an extrapolation technique that combines results from the trapezoidal rule with successively smaller step sizes to obtain a more accurate approximation of the definite integral of a function. The method is iterative, and it successively reduces the step size until and provides a more accurate result.

This program demonstrates numerical integration using Romberg Integration.

## How it Works

- The `main()` function demonstrates Romberg Integration by integrating a sample function over a specified interval, specifying the level of extrapolation, and comparing the result with the exact integral. It shows the numerical result and the error.

- The `romberg_integration(f, a, b, levels)` function takes as input the function to be integrated, the lower and upper limits of the integration interval, and the number of extrapolation levels. The function then:
    - Initializes a matrix to store the intermediate results of the integration.
    - Calls the `trapezoidal` function at different step sizes to fill the matrix with estimates.
    - Extrapolates the estimates to achieve higher accuracy and returns the result.


## Program Input & Output
 
For example, say you want to integrate the equation $f(t) = 2t e^{-t}$ with the limits $a=0$ and $b=1$. With the exact integral $\int_{a}^{b} f(t) dt = -2t - 2e^{-t}$.

When you run the program, `romberg_integration.py`, the output will look like this:

```

Numerical Integration using Romberg Integration

For 5 iterations:
Numerical result: 0.5284822353142307
Exact result: 0.5284822353142307
Error: 0.000000e+00
```