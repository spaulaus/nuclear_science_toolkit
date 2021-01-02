"""
file: time-of-flight-calculator.py
brief:
author: S. V. Paulauskas
date: January 02, 2021
"""
from nuclear_science_toolkit.physical_constants import SPEED_OF_LIGHT


def calculate_time_of_flight(mass, energy, distance):
    """

    :param mass: Mass of particle in in MeV/c**2
    :param energy: The particle energy in MeV
    :param distance: Distance the particle traveled in meters.
    :return:
    """
    return (distance / SPEED_OF_LIGHT) * (mass / (2 * energy))


def calculate_energy(mass, time_of_flight, distance):
    """

    :param mass: Mass of particle in in MeV/c**2
    :param time_of_flight: Flight time of particle in seconds
    :param distance: Distance the particle traveled in meters.
    :return:
    """
    return 0.5 * mass * (distance / time_of_flight) ** 2

