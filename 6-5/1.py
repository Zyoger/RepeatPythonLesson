# global s
from typing import Final
from math import pi

CONSTANT_PI: Final = pi
s = 0


def cylinder(r, h, mode=True):
    """*****"""
    global s
    global CONSTANT_PI

    def circle(r):
        """*****"""
        return CONSTANT_PI * 2 * r

    if mode:
        s = circle(r)*2 + 2*CONSTANT_PI*r*h
    else:
        s = 2*CONSTANT_PI*r*h
    return s


print(cylinder(2, 4))
print(cylinder(2, 4, mode=False))
print(s)
