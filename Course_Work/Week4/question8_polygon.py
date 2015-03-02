__author__ = 'thijn'
# -*- coding: utf-8 -*-
import math
# There are several ways to calculate the area of a regular polygon.
# Given the number of sides, n, and the length of each side, s,
# the polygon's area is ¼ n s2 / tan(π/n).
#
# For example, a regular polygon with 5 sides, each of length 7 inches,
# has area 84.3033926289 square inches.
#
# Write a function that calculates the area of a regular polygon,
# given the number of sides and length of each side.
# Submit the area of a regular polygon with 7 sides each of length 3 inches.
# Enter a number (and not the units) with at least four digits of precision after the decimal point.
#
# Note that the use of inches as the unit of measurement in these examples is arbitrary.
# Python only keeps track of the numerical values, not the units.
# n = number  of sided
# s = length of each side.


def polygon_area(n, s):
    print "number of sides %s: " % n
    print "length of those sides %s: " % s
    pi = 3.14
    area = (0.25 * n * s ** 2) / (math.tan(math.pi / n))
    print area


polygon_area(7,3)
polygon_area(5,7)
