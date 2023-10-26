import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')


def main():
    '''Main function to perform linear regression and plot the results.'''

    print('\nLinear Regression using the method of Least Squares.\n')

    # Example data points
    x = np.linspace(0, 1, 101)
    y = 1 + x + x * np.random.random(len(x))

    # Calculate the best-fit line
    slope, y_intercept = line_fit(x, y)

    print(f'Best-Fit Line: y = {slope:.4f}x + {y_intercept:.4f}')

    # Plot the results
    plot_results(x, y, slope, y_intercept)


def line_fit(x, y):
    '''
    Perform linear regression to find the best-fit line parameters.

    Parameters:
        x (numpy.ndarray): Array of x-values (independent variable).
        y (numpy.ndarray): Array of y-values (dependent variable).

    Returns:
        tuple: A tuple containing the slope and y-intercept of the best-fit line.
    '''
    # Calculate the mean of x-values
    x_average = x.mean()
    
    if (x * (x - x_average)).sum() == 0:
        # If the denominator is zero, data points are collinear
        return None, None
    else:
        # Calculate the slope using the method of least squares
        slope = (y * (x - x_average)).sum() / (x * (x - x_average)).sum()
        # Calculate the y-intercept
        y_intercept = y.mean() - slope * x_average

    return slope, y_intercept  # Return the calculated slope and y-intercept


def plot_results(x, y, slope, y_intercept):
    '''
    Plot the data, best-fit line, and display results.

    Parameters:
        x (numpy.ndarray): Array of x-values (independent variable).
        y (numpy.ndarray): Array of y-values (dependent variable).
        slope (float): The slope of the best-fit line.
        y_intercept (float): The y-intercept of the best-fit line.
    '''
    plt.figure(figsize=(8, 6))

    # Plot the data points
    plt.scatter(x, y, color='cyan', label='Data Points')

    # Plot the best-fit line
    x_range = np.linspace(min(x), max(x), 100)
    y_fit = slope * x_range + y_intercept
    plt.plot(x_range, y_fit, color='orange', label=f'Best-Fit Line: y = {slope:.4f}x + {y_intercept:.4f}')

    # Display the results on the plot
    plt.legend()
    plt.title('Linear Regression')
    plt.xlabel('$x$')
    plt.ylabel('$y$')

    plt.show()


if __name__ == '__main__':
    main()