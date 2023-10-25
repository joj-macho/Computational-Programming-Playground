# Numerical Integration using the Composite Midpoint Method

## Description

Numerical integration is a technique for approximating the definite integral of a function over a given interval. The Composite Midpoint Method is one such numerical integration method. It works by approximating the integral of a function as the sum of areas of rectangles with midpoints on the curve.

The formula for the Composite Midpoint Method for numerical integration is as follows:
$$\int_{a}^{b} f(x) dx \approx h \sum_{i=0}^{n-1}f \left(a + \frac{h}{2} + ih \right) $$

where:
- $a$ and $b$ are the lower and upper limits of the integration interval.
- $n$ is the number of subintervals (or rectangles).
- $h$ is the width of each subinterval and is calculated as $h = \frac{b - a}{n}$.
- $f(x)$ is the function to be integrated.

This program demonstrates numerical integration using the Composite Midpoint Method.

## How it Works

- The `main()` function demonstrates the Composite Midpoint Method by integrating a sample function over a specified interval and comparing the result with the exact integral, showing the numerical result and the error.

- The `midpoint(f, a, b, n)` function takes as input the function to be integrated, the lower and upper limits of the integration interval, and the number of subintervals. Then:
    - The function calculates the width of each subinterval (`h`) and initializes the sum of function evaluations at zero.
    - It then loops through the subintervals, evaluating the function at the midpoints of each subinterval and adding the values to the sum.
    - The Composite Midpoint Method formula is applied, and the result is returned as the numerical approximation of the integral.


## Program Input & Output
 
For example, say you want to integrate the equation $f(t) = 2t e^{-t}$ with the limits $a=0$ and $b=1$. With the exact integral $\int_{a}^{b} f(t) dt = -2t - 2e^{-t}$.

When you run the program, `composite_midpoint.py`, the output will look like this:

```

Numerical Integration using the Composite Midpoint Method.

For n = 20 subintervals:
Numerical result: 0.5286905342550723
Exact result: 0.5284822353142307
Error: 2.082989e-04
```