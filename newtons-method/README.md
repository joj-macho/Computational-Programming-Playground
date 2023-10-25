# Newton-Raphson Root Finding Method

## Description

The Newton-Raphson method is an iterative technique for finding the roots of a given function. The method uses the concept of derivatives to approximate the location of roots. Given a function $f(x)$, we want to find $x$ such that $f(x)=0$.

The Newton-Raphson method begins with an initial guess for the root, denoted as $x_0$​. It then iteratively refines this guess using the Newton-Raphson iteration formula:
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$
where $x_{n+1}$ is the updated guess for the root, $x_{n}$ is the current guess for the root, $f(x_n)$ is the function value at the current guess, and $f'(x_n)$ is the derivative of the function at the current guess.

The method continues iterating until the function value is within the desired accuracy ($\epsilon$) or a maximum number of iterations is reached.

This program implements the Newton-Raphson method to find the roots of a given function.

## How It Works

- The program starts by defining the `main` function. The `newton_raphson` function is the core of this method, used to find the root of a given function within the interval $[a, b]$ using the Newton-Raphson method with a numerical derivative.

- The `newton_raphson` function is used to find the root of a given function `f` within the interval [a, b] by the Newton-Raphson method using the numerical derivative. Here's how it works
    - `newton_raphson` takes `f` as the function to be analyzed, an interval $[a, b]$ for the root search, and an initial guess `x` for the root.
    - The precision `eps` and the maximum number of iterations `max_iterations` are specified.
    - It starts with the initial guess `x` and calculates the function value `f(x)`.
    - The method then computes a derivation step `dx` and approximates the derivative of the function `df`.
    - The root correction `dx` is determined, and the approximation `x` is updated.
    - If the updated root `x` falls outside the interval $[a, b]$, the function returns an error code 1, indicating that the interval does not contain a root.
    - If the root is considered converged (meaning the change in the root is smaller than the specified tolerance), the function returns the root and a success code 0, along with the number of iterations it took.
    - If the maximum number of iterations is reached without convergence, an error code 2 is returned, indicating that the maximum number of iterations were exceeded.

## Program Input & Output

When you run the program, `newton_method.py`, the output will look like this:

for $f(x) = x^2 - 2$, Interval $[-10, 10]$ with step $0.1$, and desired accuracy $\epsilon = 1 \times 10^{-6}$

```

Finding Roots using Newton-Raphson Method with Numerical Derivative

Root: -1.41421 found in interval (-1.50, -1.40) after 4 iterations.
Root: 1.41421 found in interval (1.40, 1.50) after 4 iterations.
```