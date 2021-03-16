#!/usr/bin/env python3

import sys
import math
from display_x import *

def calc_sec(argv):
    a = [float(argv[2]), float(argv[3]), float(argv[4]), float(argv[5]), float(argv[6])]
    x = 1.0
    xb = 0
    c = 0
    while c <= 1000 and abs(a[4] * x ** 4 + a[3] * x ** 3 + a[2] * x ** 2 + a[1] * x + a[0]) > 10 ** -int(argv[7]):
        f = a[4] * x ** 4 + a[3] * x ** 3 + a[2] * x ** 2 + a[1] * x + a[0]
        fb = a[4] * xb ** 4 + a[3] * xb ** 3 + a[2] * xb ** 2 + a[1] * xb + a[0]
        if (f - fb) == 0 or (f * (x - xb)) == 0:
            return 84
        res = x - (((f * (x - xb)) / (f - fb)))
        xb = x
        x = res
        display_result(x, argv)
        c += 1