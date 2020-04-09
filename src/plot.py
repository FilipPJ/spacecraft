import matplotlib.pyplot as plt
import numpy as np
import math

from resolution import calculate_diffracion_limit as clc

WAVELENGTHS = {"red": (670, "red"), "green": (530, "green"), "blue": (470, "blue"), "infrared": (800, "magenta")}
DIAMETER = (8, 18)
DISTANCES = np.arange(200, 2000, 1)
SCENARIOS = (1, np.sin(math.degrees(80)))


def plot() -> None:
    _, axs = plt.subplots(2, 2)

    for i, d in enumerate(DIAMETER):
        for j, s in enumerate(SCENARIOS):
            for label, (wl, color) in WAVELENGTHS.items():
                axs[j][i].plot(DISTANCES / s, clc(wl, DISTANCES / s, d), label=label, color=color)
            axs[j][i].set_title(f"Diffraction limit of lens for lens diameter {d} [cm] for scenario {j+1}")
            axs[j][i].set_xlabel("Distance [km]")
            axs[j][i].set_ylabel("Diffraction limit [m]")
            axs[j][i].legend()

    plt.show()  # used to block after plot so script does not exit to early


if __name__ == "__main__":
    plot()
