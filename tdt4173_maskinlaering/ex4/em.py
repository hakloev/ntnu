import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from math import exp as euler
from math import sqrt
from math import pi as PI


MAX_ITERATIONS = 1000
COLORS = [
    'red',
    'blue',
    'yellow',
    'purple'
]


def load_data(filename):
    """
    Loads the data from filename in the data-folder
    :param filename: The filename to load
    :return: The data as floats in a list
    """
    data = []
    with open('data/' + filename) as raw_data:
        for line in raw_data.readlines():
            data.append(float(line.strip('\n')))
    return data
    # data = np.mat(np.genfromtxt('data/' + filename)).T
    # return data


def visualize_data(data, mu):
    """
    Visualizes the data in a histogram
    :param data: The entire data set
    :param mu: The mean values as a list
    :return: None
    """
    n, bins, patches = plt.hist(data, len(data), normed=True, color='green')
    plt.xlim(min(data), max(data))

    for mu_i in range(len(mu)):
        y = mlab.normpdf(bins, mu[mu_i], 1)
        l = plt.plot(bins, y, COLORS[mu_i], linewidth=2, label='$\mu_{%i}$' % mu_i)
    mu_str = ''.join([' \mu_{%i}=%.3f, ' % (i, mu[i]) for i in range(len(mu))])

    plt.legend()
    plt.title(r'$\mathrm{Histogram\ of\ sample\ data:}\ %s\ \sigma=%.1f$' % (mu_str, 1))
    plt.show(block=True)


def m_step(expected_values, data, j):
    """
    Calculates u_j (maximum likelihood) with the expected values from the E-step
    :param expected_values: The expected values from the E-step
    :param data: The data set
    :param j: The index of the mean currently working on
    :return: The maximum likelihood
    """
    return sum([expected_values[j][i] * data[i] for i in range(len(data))]) / sum(expected_values[j])


def pdf_n(data, means, x, mu, sigma):
    """
    Calculates the probability density for the given input parameters
    :param data: The data set
    :param means: The current means
    :param x: The index of the xth element in the data set
    :param mu: The index of the mean to use
    :param sigma: The variance, 1 in this case
    :return: The result of pdf_N
    """
    nominator = euler(-(((data[x] - means[mu]) ** 2) / (2 * sigma)))
    denominator = sqrt(sigma) * sqrt(2 * PI)
    return nominator / denominator


def em(means=None, filename='sample-data.txt', visualize=False):
    """
    Implementation of the EM algorithm for Gaussian Mixtures
    :param means: If provided, this means will be used instead of the default [min, max] of the data
    :param filename: The filename to load from the data-folder
    :param visualize: If the result should be presented as a histogram using matplotlib
    :return: None
    """
    data = load_data(filename)
    if means is None:
        means = [min(data), max(data)]
    num_of_mixtures, dimensions = len(data), 1  # Number of mixtures, dimension of mixture
    num_of_measures = len(means)  # Number of Gaussians

    for iteration in range(1, MAX_ITERATIONS + 1):
        if iteration % 5 == 0 or iteration == 1:
            print('%i: %s' % (iteration, means))

        """
        E-Step
        Calculates the expected values for every hidden variable given the current hypothesis
        Does this for every Gaussian
        """
        expected_values = []
        for j in range(num_of_measures):
            inner_values = []
            for i in range(num_of_mixtures):
                pdf_n_denominator = pdf_n(data, means, i, j, 1)
                sum_ = sum([pdf_n(data, means, i, n, 1) for n in range(num_of_measures)])
                inner_values.append(pdf_n_denominator / sum_)
            expected_values.append(inner_values)

        """
        M-Step
        Described in the method m_step()
        """
        temp = [m_step(expected_values, data, j) for j in range(num_of_measures)]

        if temp == means:
            # The algorithm has converged and can be terminated
            print('Converged at %i' % iteration)
            break
        means = temp
    if visualize:
        visualize_data(data, means)


if __name__ == "__main__":
    em(visualize=True)
