#!/usr/bin/env python3

import sys
import math
from bisection import *
from newton import *
from secant import *

def display_h(argv):
    if argv[1][0] == '-' and argv[1][1] == 'h' and len(argv[1]) == 2:
        print("USAGE")
        print("\t./105torus opt a0 a1 a2 a3 a4 n")
        print("DESCRIPTION")
        print("\topt             method option:")
        print("\t                \t1 for the bisection method")
        print("\t                \t2 for Newton’s method")
        print("\t                \t3 for the secant method")
        print("\ta[0-4]\tcoefficients of the equation")
        print("\tn     \tprecision (the application of the polynomial to the solution should")
        print("\t      \tbe smaller than 10ˆ-n)")
        return 1
    return 0

def error(argv):
    if len(argv) < 8 or len(argv) > 8:
        sys.stderr.write("Error: not enough/too many argument\n")
        return 84
    if len(argv[1]) > 1:
        sys.stderr.write("SyntaxError: invalid syntax\n")
        return 84
    for i in range(1, len(argv)):
        for x in range(0, len(argv[i])):
            if ((argv[i][x] < '0' or argv[i][x] > '9') and argv[i][0] != '-' and argv[i][x] != '.'):
                sys.stderr.write("SyntaxError: invalid syntax\n")
                return 84
    if (argv[7][0] == '-' or int(argv[7]) == 0):
        sys.stderr.write("Error: wrong argument\n")
        return 84
    return 0

def main(argv):
    if len(argv) == 1:
        sys.stderr.write("Error: not enough argument\n")
        return 84
    if display_h(argv) == 1:
        return 0
    if error(argv) == 84:
        return 84
    if argv[1][0] == '1':
        calc_bis(argv)
        return 0
    if argv[1][0] == '2':
        calc_new(argv)
        return 0
    if argv[1][0] == '3':
        calc_sec(argv)
        return 0
    sys.stderr.write("Error")
    return 84