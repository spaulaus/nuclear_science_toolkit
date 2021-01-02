"""
file: positronium_lifetime_analysis.py
brief:
author: S. V. Paulauskas
date: December 24, 2020
"""
from math import pi

import numpy as np
from scipy.optimize import curve_fit


def calibrate_tac(energy):
    return 0.0058817 * energy + 1.61117


def gauss(data, *args):
    """

    :param data:
    :param args:
    :return:
    """
    norm, mu, sigma = args
    return (norm / (sigma ** 2 * np.sqrt(2 * pi))) * np.exp(-pow((data - mu) / sigma, 2) * 0.5)


def positronium_lifetime_function(data, *args):
    return np.piecewise(data, [data > args[1], data <= args[1]],
                        [lambda t: gauss(t, args[0], args[1], args[2]) +
                                   gauss(t, args[3], args[4], args[5]) +
                                   gauss(t, args[6], args[7], args[8]) + args[15] * t + args[16],
                         lambda t: gauss(t, args[0], args[1], args[2]) +
                                   gauss(t, args[3], args[4], args[5]) +
                                   gauss(t, args[6], args[7], args[8]) +
                                   args[9] * np.exp(args[11] * (t - args[10])) +
                                   args[12] * np.exp(args[14] * (t - args[13])) +
                                   args[15] * t + args[16]])


if __name__ == '__main__':
    from data.positronium_spectrum import spectrum
    import matplotlib.pyplot as plt

    p0 = [1000, 2500, 25,
          1000, 2500, 25,
          1000, 2500, 25,
          10, 4000, 0.1,
          10, 3500, 0.0001,
          1, 2.5]
    results, pcov = curve_fit(positronium_lifetime_function, np.array(range(0, len(spectrum))),
                              spectrum, p0=p0)

    plt.plot(spectrum, label='Data')
    plt.plot(positronium_lifetime_function(spectrum, *results), label="Fit", color='red')
    plt.legend()
    plt.show()
