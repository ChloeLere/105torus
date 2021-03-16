#!/usr/bin/env python3

import sys
import math
from display_x import *

def calc_bis(argv):
    a = [float(argv[2]), float(argv[3]), float(argv[4]), float(argv[5]), float(argv[6])]
    inter = [0, 1]
    x1 = (a[4] * inter[0] ** 4 + a[3] * inter[0] ** 3 + a[2] * inter[0] ** 2 + a[1] * inter[0] + a[0])
    x2 = (a[4] * inter[1] ** 4 + a[3] * inter[1] ** 3 + a[2] * inter[1] ** 2 + a[1] * inter[1] + a[0])
    if (x1 * x2 >= 0):
        return 84
    x = 0.5
    c = 0
    while ((abs(a[4] * x ** 4 + a[3] * x ** 3 + a[2] * x ** 2 + a[1] * x + a[0]))) > (10 ** (-(int(argv[7])))) and c < 1000:
        x = (inter[0] + inter[1]) / 2
        xm = (a[4] * x ** 4 + a[3] * x ** 3 + a[2] * x ** 2 + a[1] * x + a[0])
        x1 = (a[4] * inter[0] ** 4 + a[3] * inter[0] ** 3 + a[2] * inter[0] ** 2 + a[1] * inter[0] + a[0])
        x2 = (a[4] * inter[1] ** 4 + a[3] * inter[1] ** 3 + a[2] * inter[1] ** 2 + a[1] * inter[1] + a[0])
        if xm == 0:
            display_result(x, argv)
        if x1 * xm < 0:
            display_result(x, argv)
            inter[1] = x
        if x1 * xm >= 0:
            display_result(x, argv)
            inter[0] = x
        c += 1