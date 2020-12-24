"""
file: compton_calculations.py
brief:
author: S. V. Paulauskas
date: December 24, 2020
"""
from math import cos, pi, log

from numpy import arange

from nuclear_science_toolkit.physical_constants import ELECTRON_MASS, ELECTRON_RADIUS


def calculate_compton_edge(energy):
    """
    Calculate the maximum Compton energy in keV given an input gamma energy in keV.
    :param energy: Incident gamma energy in keV.
    :return: Maximum compton energy that the gamma can obtain.
    """
    return calculate_compton_energy(energy, 180)


def calculate_compton_energy(energy, angle):
    """
    return (energy/(1.+(1-math.cos(theta))*energy/511.))
    :param energy: Incident gamma ray energy in keV.
    :param angle: Incident gamma ray angle in degrees.
    :return:
    """
    return energy - energy / (
            1. + (1 - cos(angle * (pi / 180))) * energy / (ELECTRON_MASS['value'] * 1000))


def calculate_klein_nishia(energy):
    """
    double gammaEnergy = 1.275;
    double resPercent = 0.05;
    double integrationMax = 1e4;
    double sigma = gammaEnergy*resPercent;
    ofstream outFile("out.dat");

    double me = consts.GetConstant("electronMass").GetValue();
    double c = consts.GetConstant("c").GetValue();
    double re = consts.GetConstant("electronRadius").GetValue();
    double a = gammaEnergy/me;
    double coeff = (M_PI/me)*pow(re/a/c, 2);

    double comptonEdge = CalculateComptonEdge(gammaEnergy);
    double integral = 0.0;

    double stepSize = 0.001;
    double maxT = gammaEnergy - stepSize;

    for(double T = 0.0; T < maxT; T += stepSize) {
        double s = T/gammaEnergy;
        double pt0 = pow(s/(a*(1-s)), 2);
        double pt1 = (s/(1-s))*(s-(2/a));
        double sigT = (2 + pt0 + pt1);

        //double spread = 0.5*( erf(s/))

        integral = 0.0;
        if(resPercent != 0.0) {
            for(double X = 0; X <= integrationMax; X += stepSize) {
                double gauss = exp(-pow((X-s)/sigma,2)/2);
                integral += (gauss*sigT/sigma)*stepSize;
            }
        } else
            integral = sigT;
        outFile << T << " " << integral << endl;
    }

    :param energy:
    :return:
    """
    a = energy / (ELECTRON_MASS['value'] * 1000)
    energies = list()
    cross_sections = list()
    for recoil in arange(0, calculate_compton_edge(energy), 0.001):
        energies.append(recoil)
        cross_sections.append(2 * pi * ELECTRON_RADIUS['value'] ** 2 * (
                ((1 + a) / a) * ((2 + 2 * a) / (1 + 2 * a) - (log(1 + 2 * a) / a)) + (
                log(1 + 2 * a) / 2 * a) - ((1 + 3 * a) / (1 + 2 * a) ** 2)))
    return energies, cross_sections
    # s = value / energy
    # point_0 = (s / (a * (1 - s))) ** 2
    # point_1 = (s / (1 - s)) * (s - (2 / a))
    # signal_t = 2 + point_0 + point_1


if __name__ == '__main__':
    assert 39.46 == round(calculate_compton_edge(122.06), 2)
    assert 340.67 == round(calculate_compton_edge(511), 2)
    assert 663.55 == round(calculate_compton_edge(860.56), 2)
    assert 1611.81 == round(calculate_compton_edge(1836.1), 2)
    assert 2381.75 == round(calculate_compton_edge(2614.5), 2)

    import matplotlib.pyplot as plt

    energies, cross_section = calculate_klein_nishia(662)
    plt.plot(energies, cross_section)
    plt.show()
