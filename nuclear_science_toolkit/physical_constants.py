"""
file: physical_constants.py
brief:
author: S. V. Paulauskas
date: December 24, 2020

This file simply contains a list of physical constants that are useful to us in various applications.
"""
from math import pi

ELECTRON_VOLTS_TO_JOULES = {'value': 1.602176565e-19, 'error': 0.000000035e-19, 'unit': "J/eV"}
ALPHA_MASS = {'value': 3727.379240, 'error': 0.000082, 'unit': "MeV/c^2"}
DEUTERON_MASS = {'value': 1875.612859, 'error': 0.000041, 'unit': "MeV/c^2"}
ELECTRON_MASS = {'value': 0.510998928, 'error': 0.000000011, 'unit': "MeV/c^2"}
HELION_MASS = {'value': 2808.391482, 'error': 0.000062, 'unit': "MeV/c^2"}
MUON_MASS = {'value': 105.6583715, 'error': 0.0000035, 'unit': "MeV/c^2"}
NEUTRON_MASS = {'value': 939.565379, 'error': 0.000021, 'unit': "MeV/c^2"}
PROTON_MASS = {'value': 938.272046, 'error': 0.000021, 'unit': "MeV"}
TAU_MASS = {'value': 1776.82, 'error': 0.16, 'unit': "MeV/c^2"}
TRITON_MASS = {'value': 2808.921005, 'error': 0.000062, 'unit': "MeV/c^2"}
BOHR_RADIUS = {'value': 0.52917721092e-10, 'error': 0.00000000017e-10, 'unit': "m"}
ELECTRON_RADIUS = {'value': 2.8179403267e-15, 'error': 0.0000000027e-15, 'unit': "m"}
ANGSTROM_STAR = {'value': 1.00001495e-10, 'error': 0.00000090e-10, 'unit': "m"}
AVOGADROS_NUMBER = {'value': 6.02214129e23, 'error': 0.00000027e23, 'unit': "1/mol"}
BOHR_MAGNETON = {'value': 927.400968e-26, 'error': 0.000020e-26, 'unit': "J/T"}
BOLTZMANN_CONSTANT = {'value': 8.6173324e-5, 'error': 0.0000078e-5, 'unit': "eV/K"}
SPEED_OF_LIGHT = {'value': 299792458, 'error': 0.0, 'unit': "m/s"}
ELECTRON_CHARGE = {'value': 1.602176565e-19, 'error': 3.5e-27, 'unit': "C"}
EPSILON_0 = {'value': 1. / (299792458 * 4e-7 * pi), 'error': 0.0, 'unit': "F/m"}
FARADAY = {'value': 96485.3365, 'error': 0.0021, 'unit': "C/mol"}
FERMI_COUPLING = {'value': 1.166364e-5, 'error': 0.000005e-5, 'unit': "GeV^-2"}
FINE_STRUCTURE_CONSTANT = {'value': 7.2973525698e-3, 'error': 0.0000000024e-3, 'unit': "none"}
EARTH_GRAVITY = {'value': 9.80665, 'error': 0.0, 'unit': "m/s^2"}
GRAVITATIONAL_CONSTANT = {'value': 6.67384e-11, 'error': 0.00080e-11, 'unit': "m^3*kg^-1*s^-2"}
H = {'value': 4.135667516e-15, 'error': 0.000000091e-15, 'unit': "eV*s"}
H_BAR = {'value': 6.58211928e-16, 'error': 0.00000015e-16, 'unit': "eV*s"}
JOSEPHSON = {'value': 483597.870e9, 'error': 0.011e9, 'unit': "Hz/V"}
MU_0 = {'value': 4e-7 * pi, 'error': 0.0, 'unit': "V*s/(A*m)"}
RYDBERG = {'value': 1.0973731568539e7, 'error': 0.0000000000055e-7, 'unit': "1/m"}
STEPHAN_BOLTZMANN = {'value': 5.670373e-8, 'error': 0.000021e-8, 'unit': "W*m^-2*K^-4"}
