# Newton-Raphson Root Finding Method

## Description

The Newton-Raphson method is an iterative technique for finding the roots of a given function. The method uses the concept of derivatives to approximate the location of roots. Given a function $f(x)$, we want to find $x$ such that $f(x)=0$.

The Newton-Raphson method begins with an initial guess for the root, denoted as $x_0$​. It then iteratively refines this guess using the Newton-Raphson iteration formula:
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$
where $x_{n+1}$ is the updated guess for the root, $x_{n}$ is the current guess for the root, $f(x_n)$ is the function value at the current guess, and $f'(x_n)$ is the derivative of the function at the current guess.

The method continues iterating until the function value is within the desired accuracy ($\epsilon$) or a maximum number of iterations is reached.

This program implements the Newton-Raphson method to find the roots of a given function.

## How It Works

- The program starts by defining the `main` function.

- The `newton` function implements the Newton-Raphson method to find the root of a given function.

- The method uses the derivative of the function to iteratively refine the guess for the root until the function value is within the desired accuracy or the maximum iterations are reached.

## Program Input & Output

When you run the program, `newton_method.py`, the output will look like this:

for $f(x) = x^2 - 4$, $f'(x) = 2x$, Initial guess $x_0 = 1000$, and desired accuracy $\epsilon = 1 \times 10^{-6}$
```
Number of function calls: 27
A solution is: 2.000000
```