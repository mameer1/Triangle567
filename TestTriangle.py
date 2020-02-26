# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Scalene AND Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Scalene AND Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    # tests below written by Michael Ameer

    def test0(self):
        self.assertEqual(classify_triangle(210, 160, 180),'InvalidInput')
    def test1(self):
        self.assertEqual(classify_triangle(3),'InvalidInput')
    def test2(self):
        self.assertEqual(classify_triangle(3,4,5,6),'InvalidInput')
    def test3(self):
        self.assertEqual(classify_triangle(3,'side',6),'InvalidInput')
    def test4(self):
        self.assertEqual(classify_triangle(3,-4,5),'InvalidInput')
    def test5(self):
        self.assertEqual(classify_triangle(3,4,8),'NotATriangle')
    def test6(self):
        self.assertEqual(classify_triangle(3,3,5),'Isosceles')
    def test7(self):
        self.assertEqual(classify_triangle(3,3,3*2**.5),'Isosceles AND Right')
    def test8(self):
        self.assertEqual(classify_triangle(3,5,6),'Scalene')
    def test9(self):
        self.assertEqual(classify_triangle([3],4,5),'InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

