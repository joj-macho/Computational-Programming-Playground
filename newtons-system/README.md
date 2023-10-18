# Newton's Method for Nonlinear Systems

## Description

Newton's method is an iterative root-finding technique that uses the Jacobian matrix of the system to approximate the solution. In this case, the system is represented by a set of nonlinear equations in the form $F(x)=0$, where $F$ is a vector-valued function and $x$ is the vector of unknowns.

For a scalar-valued function $f(x)$, the iteration formula is given by:
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

where $x_n$ is the current approximation, $f(x_n)$ is the function value, and $f'(x_n)$ is the derivative of the function. As described in 

For a system of nonlinear equations $F(x)=0$, where $F$ is a vector-valued function and $x$ is a vector of unknowns, the iteration formula becomes a linear system:
$$J(x_n) \cdot \Delta x_n + F(x_n) = 0$$

where $J(x_n)$ is the Jacobian matrix of $F$, $\Delta x_n$ is the update to the approximation, and $F(x_n)$ is the vector of function values.


This program demonstrates the application of Newton's method to solve a system of nonlinear equations.

## How It Works

- The program starts by defining the `main` function. Which sets up the problem by defining the system of nonlinear equations and the initial guess for the solution. It then calls `newton_system()` with the defined functions, initial guess, and desired accuracy (`eps`).

- The `newton_system()` function iteratively applies Newton's method, updating the approximation and computing the norm of the function values until the desired accuracy is achieved or a maximum number of iterations is reached.

- The results, including the solution, the number of iterations, and the intermediate results for each iteration, are displayed.


## Program Input & Output

When you run the program, `newtons_system.py`, the output will look like this:

```

```