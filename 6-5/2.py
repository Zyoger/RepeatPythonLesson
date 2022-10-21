# local s
from typing import Final
from math import pi
CONSTANT_PI: Final = pi


def cylinder(r, h, mode=True):
    """*****"""
    global CONSTANT_PI
    s = 0

    def circle(rad):
        """*****"""
        return CONSTANT_PI * 2 * rad

    if mode:
        s = circle(r)*2 + 2*CONSTANT_PI*r*h
    else:
        s = 2*CONSTANT_PI*r*h
    return s


print(cylinder(2, 4))
print(cylinder(2, 4, mode=False))
