# Bisection Method for Root Finding

## Description

The bisection method is an iterative technique for finding the roots of a given function within a specified interval. Given a function $f(x)$, we want to find $x$ such that $f(x)=0$.

The bisection method starts with an interval $[a,b]$ containing a root of the function. It then iteratively divides the interval in half, narrowing down the search for the root. That is, it follows the following methodology:

- Start with an interval $[a,b]$ such that $f(a) \times f(b)<0$ (i.e., opposite signs).
- Compute the midpoint $x_M=\frac{a+b}{2}$​.
- Evaluate $f(x_M)$ and check if $f(x_M) \times f(a)<0$ or $f(x_M) \times f(b)<0$. Update the interval accordingly.
- Repeat steps 2-3 until the function value is within the desired accuracy.


This program implements the Bisection method to find the roots of a given function.


## How it Works

- The `main()` function initiates the root finding process using the bisection method. Here the `bisection()` function is used to find the root within an interval $[a, b]$.

- The `bisection()` function implements the bisection method to find the root of a given function. This method iteratively narrows down the interval containing the root by evaluating the function at the midpoint and updating the interval based on the sign of the function value. Here's how it works
    - `eps` represents the precision or tolerance of the root, and `max_iterations` sets the maximum number of iterations.
    - The function begins by evaluating the function at both ends of the interval: `fa` at the lower limit a and `fb` at the upper limit b.
    - If `fa` or `fb` is already zero, this indicates that `a` or `b` is a root, and the function returns the respective value along with an error code of 0.
    - If `fa` and `fb` have the same sign, it means that the interval does not contain a root or contains multiple roots, leading to an error code of 1.
    - The method then proceeds to iteratively narrow down the interval by calculating the midpoint `x` and evaluating the function at this point.
    - Based on the sign of the function value at the midpoint, the interval $[a, b]$ is adjusted accordingly.
    - If the width of the interval `b - a` becomes smaller than the specified tolerance or if the function value `fx` is within the tolerance, the method returns the root, an error code of 0 to indicate success, and the number of iterations it took.
    - If the maximum number of iterations is reached without achieving convergence, an error code of 2 is returned, indicating that the maximum allowed iterations were exceeded.


## Program Input & Output

When you run the program, `bisection_method.py`, the output will look like this:

for $f(x) = x^2 - 2$, Interval $[-10, 10]$ with step $0.1$, and desired accuracy $\epsilon = 1 \times 10^{-6}$
```

Finding Roots using Bisection Method

Root: -1.41421 found in interval (-1.50, -1.40) after 16 iterations.
Root: 1.41421 found in interval (1.40, 1.50) after 16 iterations.
```