import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

def main():
    '''Main function to fit polynomials to data and plot the results.'''
    
    print('\nFitting Polynomials to Data\n')
    
    # Example data points
    x = np.linspace(0, 2*np.pi, 100)
    y = 3*np.sin(x) - 2*np.cos(x) + np.random.random(len(x))
    
    # Degrees of the polynomials to fit
    degrees = [1, 2, 3, 4]
    
    # Create subplots for each degree
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle('Fitting Polynomials to Data')
    
    for i, degree in enumerate(degrees):
        coefficients = fit_polynomial(x, y, degree)
        print(f'Coefficients (degree: {degree}): {coefficients}')
        plot_results(axs[i // 2, i % 2], x, y, coefficients, degree)
    plt.show()  # Display all the subplots


def fit_polynomial(x, y, degree):
    '''
    Fit a polynomial to data and return the polynomial coefficients.

    Parameters:
        x (numpy.ndarray): Array of x-values (independent variable).
        y (numpy.ndarray): Array of y-values (dependent variable).
        degree (int): Degree of the polynomial to fit.

    Returns:
        numpy.ndarray: Coefficients of the fitted polynomial.
    '''
    # Use polyfit function from NumPy to fit a polynomial
    coefficients = np.polyfit(x, y, degree)

    return coefficients


def plot_results(ax, x, y, coefficients, degree):
    '''
    Plot the data, the fitted polynomial, and display the polynomial equation.

    Parameters:
        ax (matplotlib.axes._subplots.Axes): Subplot to plot on.
        x (numpy.ndarray): Array of x-values (independent variable).
        y (numpy.ndarray): Array of y-values (dependent variable).
        coefficients (numpy.ndarray): Coefficients of the fitted polynomial.
        degree (int): Degree of the polynomial.
    '''
    ax.scatter(x, y, color='cyan', label='Data Points')
    y_fit = np.polyval(coefficients, x)
    ax.plot(x, y_fit, color='orange', label=f'Fitted Polynomial (Degree {degree})')
    ax.legend()
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')


if __name__ == '__main__':
    main()
