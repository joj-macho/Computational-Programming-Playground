# Secant Method for Root Finding

## Description

The secant method is an iterative technique for finding the roots of a given function. It is similar to the Newton-Raphson method but uses a secant line to approximate the root. Given a function $f(x)$, we want to find xx such that $f(x)=0$.

The secant method starts with two initial guesses for the root ($x_0$​ and $x_1$​) and iteratively refines these guesses using the secant line until the function value is within the desired accuracy or a maximum number of iterations is reached.
The secant has the following methodology:
- Start with two initial guesses ($x_0$​ and $x_1$​) for the root.
- Compute function values at $x_0$ and $x_1$​ ($f(x_0)$ and $f(x_1)$).
- Compute the new approximation for the root using the secant line formula:
$$x = x_1 - \frac{f(x_1)(x_1 - x_0)}{f(x_1) - f(x_0)}$$
- Update $x_0$​ and $x_1$​ for the next iteration.
- Repeat steps 2-4 until the function value is within the desired accuracy or a maximum number of iterations is reached.


This program implements the Secant method to find the roots of a given function.

## How It Works

- The program starts by defining the `main` function.

- The `secant` function implements the secant method to find the root of a given function.

- The method iteratively refines the guess for the root using the secant line formula until the function value is within the desired accuracy or the maximum iterations are reached.

## Program Input & Output

When you run the program, `secant_method.py`, the output will look like this:

for $f(x) = x^2 - 4$, $f'(x) = 2x$, Initial guesses $x_0 = 1000$, $x_1 = x_0 - 1$, and desired accuracy $\epsilon = 1 \times 10^{-6}$
```
Number of function calls: 19
A solution is: 2.000000
```