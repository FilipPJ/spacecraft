import matplotlib.pyplot as plt
import numpy as np

from resolution import calculate_diffracion_limit as clc

WAVELENGTHS = {"red": (670, "red"), "green": (530, "green"), "blue": (470, "blue"), "infrared": (800, "magenta")}
DIAMETER = np.arange(0.1, 10, 0.1)
DISTANCES = (200, 250)


def plot() -> None:
    _, axs = plt.subplots(2, 1)

    for i, d in enumerate(DISTANCES):
        for label, (wl, color) in WAVELENGTHS.items():
            axs[i].plot(DIAMETER, clc(wl, d, DIAMETER), label=label, color=color)
        axs[i].set_title(f"Diffraction limit of lens for distance {d} km")
        axs[i].set_xlabel("Lens diameter [cm]")
        axs[i].set_ylabel("Diffraction limit [m]")
        axs[i].legend()

    plt.show()  # used to block after plot so script does not exit to early


if __name__ == "__main__":
    plot()
