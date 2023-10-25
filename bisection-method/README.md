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

- The `main()` function initiates the root finding process using the bisection method.
- The `bisect()` function implements the bisection method to find the root of a given function.
- The method iteratively narrows down the interval containing the root by evaluating the function at the midpoint and updating the interval based on the sign of the function value.


## Program Input & Output

When you run the program, `bisection_method.py`, the output will look like this:

for $f(x) = x^2 - 2$, Interval $[-10, 10]$ with step $0.1$, and desired accuracy $\epsilon = 1 \times 10^{-6}$
```

Finding Roots using Bisection Method

Root: -1.41421 found in interval (-1.50, -1.40) after 16 iterations.
Root: 1.41421 found in interval (1.40, 1.50) after 16 iterations.
```