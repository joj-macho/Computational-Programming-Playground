import numpy as np

def main():
    '''Main function to perform linear regression using the method of least squares.'''

    print('\nLinear Regression using the method of Least Squares.\n')

    # Example data points (replace with your own dataset)
    x = np.linspace(0, 1, 101)
    y = 1 + x + x * np.random.random(len(x))

    # Calculate the best-fit line
    slope, y_intercept = line_fit(x, y)

    print(f'Best-Fit Line: y = {slope:.4f}x + {y_intercept:.4f}')


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


if __name__ == '__main__':
    main()