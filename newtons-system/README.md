# Newton's Method for Nonlinear Systems

## Description

Newton's method is an iterative root-finding technique that uses the Jacobian matrix of the system to approximate the solution. In this case, the system is represented by a set of non-linear equations in the form $\mathbf{F(x)}=0$, where $\mathbf{F}$ is a vector-valued function and $\mathbf{x}$ is the vector of unknowns.

As described before in [Newton-Raphson Root Finding Method](https://github.com/joj-macho/Computational-Programming-Playground/tree/main/newtons-method),
for a scalar-valued function $f(x)$, the iteration formula is given by:
$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

where $x_n$ is the current approximation, $f(x_n)$ is the function value, and $f'(x_n)$ is the derivative of the function. 

For a system of nonlinear equations $\mathbf{F(x)}=0$, where $\mathbf{F}$ is a vector-valued function and $\mathbf{x}$ is a vector of unknowns, the iteration formula becomes a linear system:
$$J(x_n) \cdot \Delta x_n + F(x_n) = 0$$

where $J(x_n)$ is the Jacobian matrix of $F$, $\Delta x_n$ is the update to the approximation, and $F(x_n)$ is the vector of function values.

This program demonstrates the application of Newton's method to solve a system of nonlinear equations.

## How It Works

- The program starts by defining the `main` function. Which sets up the problem by defining the system of nonlinear equations and the initial guess for the solution. It then calls `newton_system()` with the defined functions, initial guess, and desired accuracy (`eps`).

- The `newton_system()` function iteratively applies Newton's method, updating the approximation and computing the norm of the function values until the desired accuracy is achieved or a maximum number of iterations is reached.

- The program `newton_system_2.py` uses the `calculate_jacobian()` function to calculate the Jacobian matrix. This function uses finite differences to approximate the derivatives.

- The results, including the solution, the number of iterations, and the intermediate results for each iteration, are displayed.


## Program Input & Output

Consider the following example of system of equations:
$$
F_0(x_0, x_1) = x^2 - y + x \cos(\pi x) \\
F_1(x_0, x_1) = yx + e^{-y} - x^{-1}
$$

with a jacobian given by $\Delta \mathbf{F} = \mathbf{J}$:
$$
\mathbf{J} = 
\left( \begin{array}{cc}
\frac{\partial F_0}{\partial x_0} & \frac{\partial F_0}{\partial x_1} \\
\frac{\partial F_1}{\partial x_0}& \frac{\partial F_1}{\partial x_1}
\end{array} \right)
=
\left( \begin{array}{cc}
2x_0 + \cos(\pi x_0) - \pi x_0 \sin(\pi x_0) & -1 \\
x_1 + x_{0}^{-2} & x_0 - e^{-x_1}
\end{array} \right)
$$

Which can be solved by the the `newtons_system.py` and `newtons_system_2.py` programs, the output will look like this:


```
Solution:
[ 1.00000006e+00 -1.00943962e-06]

Number of iterations: 4

Results for each iteration:
Iteration 1: (array([0.89213598, 0.46067992]), array([-0.50617586, -0.07906165]))
Iteration 2: (array([ 1.01692001, -0.05679316]), array([0.07543579, 0.01732125]))
Iteration 3: (array([ 1.00042416, -0.00123474]), array([0.00165996, 0.00042422]))
Iteration 4: (array([ 1.00000006e+00, -1.00943962e-06]), array([1.06818098e-06, 5.87417811e-08]))

Norm of error: 1.0111473146330377e-06
Error within tolerance.
```