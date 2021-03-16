#!/usr/bin/env python3

import sys
import math

def display_result(x, argv):
    if len(str(x)) < int(argv[7]) + 2:
        print("x =", x)
    else:
        print("x = {:.{n}f}".format(x,n = int(argv[7])))