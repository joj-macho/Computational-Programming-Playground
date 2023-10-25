# Numerical Integration using Simpson's Rule

## Description

Numerical integration is a technique for approximating the definite integral of a function over a given interval. Simpson's Rule is one such method used for this purpose. It provides a more accurate approximation of the integral compared to the trapezoidal rule. The method works by approximating the function within each sub-interval with a quadratic polynomial and then integrating these polynomials to calculate the integral.

The formula for Simpson's Rule for numerical integration is as follows:
$$\int_{a}^{b} f(x) dx \approx \frac{h}{3} \left[f(a) + 4 \sum_{i=0, i \ \text{odd}}^{n-1} f(x_i) + 2 \sum_{i=2, i \ \text{even}}^{n-2} f(x_i) + f(b) \right]$$

where:
- $a$ and $b$ are the lower and upper limits of the integration interval.
- $n$ is the number of subintervals, and it must be an even number.
- $h$ is the width of each subinterval and is calculated as $h = \frac{b-a}{n}$.
- $x_i$ are the equally spaced points within the interval, given by $x_i = a + ih$.
- $f(x)$ is the function to be integrated.

This program demonstrates numerical integration using Simpson's Rule.

## How it Works

- The `main()` function demonstrates Simpson's Rule by integrating a sample function over a specified interval, ensuring that the number of subintervals is even, and comparing the result with the exact integral. It shows the numerical result and the error.

- The `simpsons_rule(f, a, b, n)` function takes as input the function to be integrated, the lower and upper limits of the integration interval, and the number of subintervals (which must be even). The function then:
    - Calculates the width of each subinterval (`h`) and initializes the sum to zero.
    - Loops through the subintervals, evaluating the function at equally spaced points within each subinterval and adding the values to the sum.
    - Applies the Simpson's Rule formula to compute and return the result as the numerical approximation of the integral.


## Program Input & Output
 
For example, say you want to integrate the equation $f(t) = 2t e^{-t}$ with the limits $a=0$ and $b=1$. With the exact integral $\int_{a}^{b} f(t) dt = -2t - 2e^{-t}$.

When you run the program, `simpsons_rule.py`, the output will look like this:

```

Numerical Integration using the Composite Midpoint Method.

For n = 20 subintervals:
Numerical result: 0.5286905342550723
Exact result: 0.5284822353142307
Error: 2.082989e-04
```