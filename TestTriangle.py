# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testScaleneTriangleB(self): 
        self.assertEqual(classifyTriangle(5,8,4),'Scalene','5,8,4 is a Scalene triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsocelesTriangles(self): 
        self.assertEqual(classifyTriangle(1,2,2),'Isoceles','1,2,2 should be Isoceles')
		
    def testInvalidInput(self): 
        self.assertEqual(classifyTriangle(1,-1,1),'InvalidInput','1,-1,1 should be InvalidInput')
        self.assertEqual(classifyTriangle(1,201,201),'InvalidInput','1,201,201 should be InvalidInput')

    def testNotATriangle(self): 
        self.assertEqual(classifyTriangle(1,5,9),'NotATriangle','1,5,9 should be NotATriangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

