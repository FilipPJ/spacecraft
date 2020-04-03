import matplotlib.pyplot as plt
import numpy as np

from resolution import calculate_diffracion_limit as clc

WAVELENGTHS = {"red": (670, "red"), "green": (530, "green"), "blue": (470, "blue"), "infrared": (800, "magenta")}
DIAMETER = (8, 18)
DISTANCES = np.arange(200, 2000, 1)


def plot() -> None:
    _, axs = plt.subplots(2, 1)

    for i, d in enumerate(DIAMETER):
        for label, (wl, color) in WAVELENGTHS.items():
            axs[i].plot(DISTANCES, clc(wl, DISTANCES, d), label=label, color=color)
        axs[i].set_title(f"Diffraction limit of lens for lens diameter {d} [km]")
        axs[i].set_xlabel("Distance [km]")
        axs[i].set_ylabel("Diffraction limit [m]")
        axs[i].legend()

    plt.show()  # used to block after plot so script does not exit to early


if __name__ == "__main__":
    plot()
