import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')


def main():
    '''Main function to solve an ordinary differential equation (ODE) using the Forward Euler method.'''
    
    # Define the ODE function, initial value, time step, and total time
    f = lambda u, t: -0.05 * u + 2.0  # Example ODE: du/dt = -0.05*u + 2
    u_0 = 0.0  # Initial value
    t_total = 100.0  # Total time

    # List of time steps to consider
    dt_values = [1, 5, 10, 15]
    
    # Create subplots
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    fig.suptitle('Numerical and Analytical Solutions for Different Time Steps')

    for i, dt in enumerate(dt_values):
        # Solve the ODE 
        numerical_solution, time_points = ode_forward_euler(f, u_0, t_total, dt)
        
        # Plot numerical and analytical solutions
        axs[i // 2, i % 2].plot(time_points, numerical_solution, c='w', label='Numerical Solution')
        axs[i // 2, i % 2].plot(time_points, 40*(1-np.exp(-0.05*time_points)), c='g', linestyle='dashed', label='Exact Solution')
        axs[i // 2, i % 2].set_xlabel('$t$')
        axs[i // 2, i % 2].set_ylabel('$f\,(u, t)$')
        axs[i // 2, i % 2].set_title(f'$dt = {dt}$')
        axs[i // 2, i % 2].legend()

    plt.tight_layout()
    plt.show()


def ode_forward_euler(f, u_0, t_total, dt):
    '''
    Solve an ordinary differential equation (ODE) using the Forward Euler method.

    Parameters:
        f (function): The ODE function, which takes u and t as arguments.
        u_0 (float): The initial value of the ODE.
        dt (float): The time step.
        t_total (float): The total time for the simulation.

    Returns:
        tuple: A tuple containing the numerical solution (u) and time points (t).
    '''
    n_time_steps = int(round(t_total / dt))  # Calculate the number of time steps
    u = np.zeros(n_time_steps + 1)  # Initialize an array to store the numerical solution
    t = np.linspace(0, n_time_steps * dt, len(u))  # Create an array for time points
    u[0] = u_0  # Set the initial value
    for n in range(n_time_steps):
        # Use the Forward Euler method to update the solution
        u[n + 1] = u[n] + dt * f(u[n], t[n])

    return u, t


if __name__ == '__main__':
    main()
