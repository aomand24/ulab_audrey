# star_visibility.py
import numpy as np
def star_distance(angle):
# uses parallax angle in parsecs and returns distance of star from earth in AU
    distance = 1/angle
    return distance


def star_luminosity(radius,temp):
# takes stars radius and temperature and returns luminosity using the luminosity formula
    sb=5.670374419*(10**-8)
    lumos = 4 * np.pi * (radius**2) * sb * (temp**4)
    return lumos


def can_be_seen(angle,radius,temp):
# takes the angle, radius, and temperature of a star and returns if it can be visible or not
    if star_luminosity(radius,temp)>100 and star_distance(angle)<100:
        print("Star can be seen")
    else:
        print("Star cannot be seen")
