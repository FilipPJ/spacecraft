# [Spacecraft Engineering]

## [Imaging system]

The task was to find maximial spatial resolution (in meters) that's dictated by diffraction limit.

To achieve that, we had to plot diffraction limits(1) for all the bands:

1. red (655 nm), 
2. green (545 nm), 
3. blue (475 nm),
4. near-infra red (845 nm)

and for two different telescope diameters (8cm and 18cm). 
Also there are two scenarios - when the satelite is pointing straight down(best case) and when it is tilted,
but not more than 10 degrees (worst case).

There are 2 files included:

_*resolution.py*_ - calculates diffraction limit 

_*plot.py*_ - plots 4 different plots (for different combination of lense diameters and scenarios) and icludes the legend.
 
 
 
(1)Diffraction limit - the minimum angular separation of two sources that can be distinguished by a telescope depends on the wavelength 
of the light being observed and the diameter of the telescope. 

![Diffraction Limit](/spacecraft/resolution.gif)
Format: ![Alt Text](url)

