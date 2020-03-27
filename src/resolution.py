import matplotlib.pyplot as plt
import unittest 
import logging

logging.basicConfig(level=logging.DEBUG)


def calculate_diffracion_limit(wavelength: float, distance: float, diameter: float):
    """
    wavelength [nm]
    distance [km] - from telescope fo earth
    diamenter [cm] - diameter of telescope

    ret [m] - diffraction limit
    """
    logging.debug(f'Wavelength: {wavelength}')
    logging.debug(f'Distance: {distance}')
    logging.debug(f'Diameter: {diameter}')
    radian_resolution = 1.22 * (wavelength * 1e-9) / (diameter * 1e-2)
    logging.debug(f'Radial resolution: {radian_resolution}')
    resolution = distance * 1e3 * radian_resolution
    return resolution

class TestDiffraction(unittest.TestCase):

    def test_diff(self):
        print(calculate_diffracion_limit(545, 200, 8))