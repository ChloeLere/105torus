#!/usr/bin/env python3

import sys
import math
from display_x import *

def calc_new(argv):
    a = [float(argv[2]), float(argv[3]), float(argv[4]), float(argv[5]), float(argv[6])]
    x = 0.5
    f = 1
    fp = 1
    c = 0
    while c <= 1000 and abs((x - (f / fp)) - x) >= 10 ** -float(argv[7]):
        f = a[4] * x ** 4 + a[3] * x ** 3 + a[2] * x ** 2 + a[1] * x + a[0]
        fp = a[4] * 4 * x ** 3 + a[3] * 3 * x ** 2 + a[2] * 2 * x + a[1]
        if fp == 0:
            return 84
        res = x - (f / fp)
        display_result(x, argv)
        x = res
        c += 1