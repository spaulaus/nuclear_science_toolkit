"""
file: duty_cycle.py
brief:
author: S. V. Paulauskas
date: January 02, 2021
"""
from math import exp


def calculate_duty_cycle(half_life, beam_on_time, beam_off_time):
    decay_constant = 0.693 / half_life
    tau = 1 / decay_constant
    n0 = 1.
    t1 = 0
    sgrow = -n0 * (decay_constant * t1 - decay_constant * beam_on_time + exp(
        - decay_constant * t1) - exp(-decay_constant * beam_on_time)) / decay_constant
    sdecay = n0 * (-1 + exp(- decay_constant * beam_on_time)) * (
            -1 + exp(decay_constant * (beam_on_time - beam_off_time))) / decay_constant
    return (sgrow + sdecay) / ((beam_off_time - t1) * n0)


if __name__ == '__main__':
    half_life = 20.1
    beam_on = 2
    beam_off = 3

    print(f'ON from 0 s to {beam_on} s || OFF {beam_on} s to {beam_off} s')
    print(f'Duty Factor = {calculate_duty_cycle(half_life, beam_on, beam_off)}')
