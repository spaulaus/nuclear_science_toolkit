"""
file: rectangular_solid_angle_calculator.py
brief: Calculator for solid angle of a rectangular solid at a given distance in centimeters.
author: S. V. Paulauskas
date: July 30, 2016
"""
import math


def calc_percent_four_pi(omega):
    """
    Calculate the solid angle as a percentage of a sphere
    :param omega: The solid angle coverage in sr.
    :return: The percentage of a sphere covered.
    """
    return omega / 4 / math.pi


def calc_array_coverage(solid_angle, number_of_bars):
    """
    Calculate the coverage for an entire array
    :param solid_angle: The solid angle in sr
    :param number_of_bars: The number of solids in the array.
    :return:
    """
    return number_of_bars * solid_angle


#
def calc_position(dimension, distance):
    """
    Define a function to calculate the ratio of the solid's dimension to the distance.
    :param dimension: The dimension that we're interested in
    :param distance: The distance to the face of the solid.
    :return:
    """
    return dimension / 2 / distance


def calculate_solid_angle(length, width, distance):
    """
    Calculates the solid angle coverage of the solid in sr. We used the following article by
    R. Mathar for the equation implemented. https://vixra.org/pdf/2001.0603v1.pdf
    :param length: The length of the solid in cm
    :param width: The width of the solid in cm
    :param distance: The distance to the solid's face in cm.
    :return: The solid angle in sr.
    """
    numerator = 1 + calc_position(length, distance) ** 2 + calc_position(width, distance) ** 2
    denominator = (1 + calc_position(length, distance) ** 2) * (
            1 + calc_position(width, distance) ** 2)
    return 4.0 * math.acos(math.sqrt(numerator / denominator))


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Rectangular solid angle calculations")
    parser.add_argument('-d', '--distance', type=float, help="The distance to the solid in cm.")
    parser.add_argument('-l', '--length', type=float, help="The length of the solid in cm.")
    parser.add_argument('-w', '--width', type=float, help="The width of the solid in cm.")
    parser.add_argument('-n', '--number_of_solids', default=1, type=int, required=False,
                        help="Number of solids to use in the calculation.")
    args = parser.parse_args()

    omega = calculate_solid_angle(args.length, args.width, args.distance)
    print("---------- Single Bar ----------")
    print("Geometric Coverage (sr) =", omega)
    print("Geometric Efficiency(abs)", calc_percent_four_pi(omega))
    print("")

    print("---------- Array Coverage ----------")
    print("Geometric Coverage (sr) =", calc_array_coverage(omega, args.number_of_solids))
    print("Geometric Efficiency(abs)",
          calc_percent_four_pi(calc_array_coverage(omega, args.number_of_solids)))
    print("")
