# Numerical Integration using the Trapezoidal Rule

## Description

Numerical integration is a technique for approximating the definite integral of a function over a given interval. The trapezoidal rule is one such method used for this purpose. The trapezoidal rule works by dividing the area under the curve of a function into a series of trapezoids. It approximates the integral by summing the areas of these trapezoids. The more trapezoids used, the closer the approximation gets to the true integral.

The formula for the trapezoidal rule for numerical integration is as follows:
$$\int_{a}^{b} f(x) dx \approx \frac{h}{2} \left[ f(a) + 2 \sum_{i=1}^{n-1} f(x_i) + f(b) \right]$$

where:
- $a$ and $b$ are the lower and upper limits of the integration interval.
- $n$ is the number of subintervals (or trapezoids).
- $h$ is the width of each subinterval and is calculated as $h = \frac{b-a}{n}$​.
- $x_i$ are the equally spaced points within the interval, given by $x_i = a + ih$.
- $f(x)$ is the function to be integrated.

This program demonstrates numerical integration using the trapezoidal rule. 

## How it Works

- The `main()` function demonstrates the trapezoidal rule by integrating a sample function over a specified interval and comparing the result with the exact integral, showing the numerical result and the error.

- The `trapezoidal(f, a, b, n)` function takes as input the function to be integrated, the lower and upper limits of the integration interval, and the number of subintervals. Then:
    - The function calculates the width of each subinterval (`h`) and initializes the sum of function evaluations at zero.
    - It then loops through the subintervals, evaluating the function at equally spaced points within each subinterval, and adding the values to the sum.
    - The trapezoidal rule formula is applied, and the result is returned as the numerical approximation of the integral.


## Program Input & Output
 
For example, say you want to integrate the equation $f(t) = 2t e^{-t}$ with the limits $a=0$ and $b=1$. With the exact integral $\int_{a}^{b} f(t) dt = -2t - 2e^{-t}$.

When you run the program, `trapezoidal_rule.py`, the output will look like this:

```

Numerical Integration using the Trapezoidal Rule.

For n = 20 subintervals:
Numerical result: 0.5280656079536598
Exact result: 0.5284822353142307
Error: 4.166274e-04
```