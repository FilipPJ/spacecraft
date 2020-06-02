import pyquaternion
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)


## Assumes that z axis is perallel to telescope axis and point to the same direction as telescope
def eci_to_quaternion(x ,y ,z):
    rotation_axis = [-y, x, 0] # perpendicular to ECI vector and z axis
    logging.info(f'Rotation_axis: {rotation_axis}')
    rotation_angle = -1 * (np.pi - np.arctan(np.sqrt(x**2 + y**2)/z))
    logging.info(f'Rotation angle: {rotation_angle}')
    q = pyquaternion.Quaternion(axis=rotation_axis, angle=rotation_angle)
    logging.info(f'Quaternion: {q}')

if __name__ == "__main__":
    eci_to_quaternion(45, 45, 45)