import numpy as np
import scipy.special
import matplotlib.pyplot as plt

def main():
    '''Main program to plot orthogonal polynomials of various order.'''

    # Use a dark background style
    plt.style.use('dark_background')
    plt.rcParams['axes.labelcolor'] = 'white'
    plt.rcParams['xtick.color'] = 'white'
    plt.rcParams['ytick.color'] = 'white'

    # Create a figure window with subplots
    fig, ax = plt.subplots(2, 2, figsize=(10, 8))

    # Define the x values for the plots
    x = np.linspace(-1, 1, 400)

    # Plot Chebyshev polynomials for orders 1 to 4
    for n in range(1, 5):
        chebyshev = scipy.special.eval_chebyt(n, x)
        ax[0, 0].plot(x, chebyshev, label=f'$T_{n}(x)$')

    ax[0, 0].set_title('Chebyshev Polynomials')
    ax[0, 0].set_xlabel('$x$')
    ax[0, 0].set_ylabel('$T_n(x)$')
    ax[0, 0].legend()

    # Plot Legendre polynomials for orders 1 to 4
    for n in range(1, 5):
        legendre = scipy.special.eval_legendre(n, x)
        ax[0, 1].plot(x, legendre, label=f'$P_{n}(x)$')

    ax[0, 1].set_title('Legendre Polynomials')
    ax[0, 1].set_xlabel('$x$')
    ax[0, 1].set_ylabel('$P_n(x)$')
    ax[0, 1].legend()

    # Plot Laguerre polynomials for orders 1 to 4
    for n in range(1, 5):
        laguerre = scipy.special.eval_laguerre(n, x)
        ax[1, 0].plot(x, laguerre, label=f'$L_{n}(x)$')

    ax[1, 0].set_title('Laguerre Polynomials')
    ax[1, 0].set_xlabel('$x$')
    ax[1, 0].set_ylabel('$L_n(x)$')
    ax[1, 0].legend()

    # Plot Hermite polynomials for orders 1 to 4
    for n in range(1, 5):
        hermite = scipy.special.hermite(n)(x)
        ax[1, 1].plot(x, hermite, label=f'$H_{n}(x)$')

    ax[1, 1].set_title('Hermite Polynomials')
    ax[1, 1].set_xlabel('$x$')
    ax[1, 1].set_ylabel('$H_n(x)$')
    ax[1, 1].legend()

    # Mark the 0 horizontal in the plot
    ax[0, 0].axhline(color="grey", ls="--", zorder=-1)
    ax[0, 1].axhline(color="grey", ls="--", zorder=-1)
    ax[1, 0].axhline(color="grey", ls="--", zorder=-1)
    ax[1, 1].axhline(color="grey", ls="--", zorder=-1)    

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
