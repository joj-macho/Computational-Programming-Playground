# False Position Method for Root Finding

## Description

The False Position Method is an iterative technique for finding the roots of a given function within a specified interval. Given a function $f(x)$, the goal is to find a value of $x$ where $f(x)$ equals zero. The method is also known as the Regula Falsi method.

The False Position Method works by iteratively narrowing down the search interval $[a, b]$ until it isolates the root. This is achieved by creating secant lines between the function values at the endpoints of the interval and finding the point where the secant line intersects the x-axis.

This program implements the False Position Method to find the roots of a given function.

## How it Works

- The program begins by defining the `main()` function. The `main` function initiates the process of finding and printing roots using the False Position Method.

- The `false_position()` function is responsible for determining a real root `x` of a function `f` isolated in the interval $[a, b]$ using the False Position Method. Here's how it works
    - The `eps` parameter sets the precision or tolerance of the root, while `max_iterations` defines the maximum number of iterations allowed.
    - The function starts by evaluating the function at both ends of the interval, calculating `fa` at the lower limit a and `fb` at the upper limit b.
    - If `fa` is already zero, it indicates that a is `a` root, and the function returns a along with an error code of 0, signifying a successful execution.
    - Likewise, if `fb` is already zero, it means that `b` is a root, and the function returns b with an error code of 0.
    - If fa and fb have the same sign, indicating that the interval $[a, b]$ does not contain a root or contains multiple roots, the function returns `b` with an error code of 1.
    - The method then enters an iterative process where it calculates a new approximation `x` based on the False Position Method. This involves creating a secant line using `a`, `b`, `fa`, and `fb` and finding the point where the secant line intersects the x-axis.
    - The function value `fx` is evaluated at this new approximation.
    - Depending on the sign of `fa * fx`, the interval $[a, b]$ is adjusted accordingly, and the method proceeds to the next iteration.
    - If the width of the interval `b - a` becomes smaller than the specified tolerance, or if the function value fx is within the tolerance, the method returns the root, an error code of 0 to indicate a successful execution, and the number of iterations it took.
    - In cases where the maximum number of iterations is reached without achieving convergence, an error code of 2 is returned, indicating that the maximum allowed iterations were exceeded.

## Program Input & Output

When you run the program, `regula_falsi_method.py`, the output will look like this;

for $f(x) = x^2 - 2$, Interval $[-10, 10]$ with step $0.1$, and desired accuracy $\epsilon = 1 \times 10^{-6}$
```

Finding Roots using False Position Method

Root: -1.41421 found in interval (-1.50, -1.40) after 4 iterations.
Root: 1.41421 found in interval (1.40, 1.50) after 4 iterations.
```