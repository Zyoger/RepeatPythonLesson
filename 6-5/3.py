# nonlocal s
from typing import Final
from math import pi
CONSTANT_PI: Final = pi


def cylinder(r, h, mode=True):
    """*****"""
    global CONSTANT_PI
    s_circle = 0

    def circle(rad):
        """*****"""
        nonlocal s_circle
        s_circle = CONSTANT_PI*2*rad

    circle(r)
    if mode:
        s = s_circle*2 + 2*CONSTANT_PI*r*h
    else:
        s = 2 * CONSTANT_PI * r * h
    return s


print(cylinder(2, 4))
print(cylinder(2, 4, mode=False))
