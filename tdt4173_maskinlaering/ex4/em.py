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
    data = []
    with open('data/' + filename) as raw_data:
        for line in raw_data.readlines():
            data.append(float(line.strip('\n')))
    return data
    # data = np.mat(np.genfromtxt('data/' + filename)).T
    # return data


def visualize_data(data, mu):
    n, bins, patches = plt.hist(data, len(data), normed=True, color='green')
    plt.xlim(min(data), max(data))

    for mu_i in range(len(mu)):
        y = mlab.normpdf(bins, mu[mu_i], 1)
        l = plt.plot(bins, y, COLORS[mu_i], linewidth=2, label='$\mu_{%i}$' % mu_i)
    mu_str = ''.join([' \mu_{%i}=%.3f, ' % (i, mu[i]) for i in range(len(mu))])

    plt.legend()
    plt.title(r'$\mathrm{Histogram\ of\ sample\ data:}\ %s\ \sigma=%.1f$' % (mu_str, 1))
    plt.show(block=True)


def e_step(data, mu, i, j):
    pass


def m_step(expected, data, j):
    sum_ = 0
    for i in range(len(data)):
        sum_ += expected[j][i] * data[i]
    return sum_ / sum(expected[j])


def pdfn(data, means, x, mu, sigma):
    nominator = euler(-(((data[x] - means[mu]) ** 2) / (2 * sigma)))
    denominator = sqrt(sigma) * sqrt(2 * PI)
    return nominator / denominator


def em(means=None, filename='sample-data.txt'):
    data = load_data(filename)
    if means is None:
        means = [min(data), max(data)]
    num_of_mixtures, dimensions = len(data), 1  # Number of mixtures, dimension of mixture
    num_of_measures = len(means)  # Number of Gaussian components

    for iteration in range(MAX_ITERATIONS):
        if iteration % 5 == 0:
            print('%i: %s' % (iteration, means))

        # E-STEP
        expected_values = []
        for j in range(num_of_measures):
            inner_values = []
            for i in range(num_of_mixtures):
                """
                nominator = euler(-(((data[i] - means[j]) ** 2) / (2 * 1)))
                denominator = 1 * sqrt(2 * PI)
                main_nominator = nominator / denominator
                """
                pdfn_denominator = pdfn(data, means, i, j, 1)

                sum_ = 0
                for n in range(num_of_measures):
                    """
                    inner_nominator = euler(-(((data[i] - means[n]) ** 2) / (2 * 1)))
                    inner_den = 1 * sqrt(2 * PI)
                    sum_ += (inner_nominator / inner_den)
                    """
                    sum_ += pdfn(data, means, i, n, 1)
                inner_values.append(pdfn_denominator / sum_)
            expected_values.append(inner_values)

        # M-STEP
        temp = [m_step(expected_values, data, j) for j in range(num_of_measures)]

        if temp == means:
            print('Converged at %i' % iteration)
            break
        means = temp
    visualize_data(data, means)


if __name__ == "__main__":
    em(means=None)
