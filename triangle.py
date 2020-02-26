# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classify_triangle(*args):
    arg_count = len(args)
    if arg_count != 3:
        return "InvalidInput"
    a = args[0]
    b = args[1]
    c = args[2]

    # verify that all 3 inputs are integers
    try:
        int(a)
        int(b)
        int(c)
    except (TypeError, ValueError):
        return "InvalidInput"

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    if (a + b <= c or a + c <= b or b + c <= a):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if a == b and b == c:
        return 'Equilateral'
    elif ((a == b and b != c) or (a == c and c != b) or (b == c and c != a)):
        if (round(a**2 + b**2, 3) == round(c**2, 3) or round(a**2 + c**2, 3) == round(b**2, 3) or round(b**2 + c**2, 3) == round(a**2, 3)):
            return "Isosceles AND Right"
        return "Isosceles"
    elif (a != b and b != c and c != a):
        if (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
            return "Scalene AND Right"
        return "Scalene"
