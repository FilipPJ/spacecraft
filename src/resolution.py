import matplotlib.pyplot as plt
import unittest 
import logging
import numpy as np

logging.basicConfig(level=logging.DEBUG)


def calculate_diffracion_limit(wavelength: float, distance: float, diameter: float) -> float:
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
        limit = calculate_diffracion_limit(545, 200, 8)
        logging.info(f"Resolution: {limit}")

    def test_diff_array(self):
        dist = np.array([200, 300])
        dia = 8
        limit = calculate_diffracion_limit(545, dist, dia)
        logging.info(f"Resolution: {limit}")

if __name__ == '__main__':
    unittest.main()