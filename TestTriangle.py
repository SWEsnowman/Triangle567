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
    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(201,201,201),'InvalidInput','InvalidInput')
    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput','InvalidInput')
    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(-1,-1,-1),'InvalidInput','InvalidInput')
    def testInvalidInputD(self):
        self.assertEqual(classifyTriangle(True,1,201),'InvalidInput','InvalidInput')
    def testInvalidInputE(self):
        self.assertEqual(classifyTriangle([1],1,2),'InvalidInput','InvalidInput')
    def testInvalidInputF(self):
        self.assertEqual(classifyTriangle('a','b','c'),'InvalidInput','InvalidInput')
        
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1,1,3),'NotATriangle','1,1,3 is not a triangle')
    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(5,2,1),'NotATriangle','5,2,1 is not a triangle')
    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(2,9,1),'NotATriangle','1,9,1 is not a triangle')

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5,12,13),'Right','5,12,13 is a Right triangle')
    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(7,24,25),'Right','7,24,25 is a Right triangle')

    def testIsocelesTriangleA(self): 
        self.assertEqual(classifyTriangle(3,3,4),'Isoceles','3,3,4 is a Isoceles Triangle')
    def testIsocelesTriangleB(self):
        self.assertEqual(classifyTriangle(150,40,150),'Isoceles','3,4,3 is a Isoceles Triangle')
    def testIsocelesTriangleC(self):
        self.assertEqual(classifyTriangle(100,7,7),'Isoceles','5,5,7 is a Isoceles Triangle')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(3,4,6),'Scalene','3,4,6 is a Scalene Triangle')
    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(5,12,14),'Scalene','5,12,14 is a Scalene Triangle')
    def testScaleneTriangleC(self):
        self.assertEqual(classifyTriangle(7,24,26),'Scalene','7,24,26 is a Scalene Triangle')
        
    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 is be equilateral')
    def testEquilateralTriangleB(self):
        self.assertEqual(classifyTriangle(100,100,100),'Equilateral','100,100,100 is be equilateral')
    def testEquilateralTriangleC(self):
        self.assertEqual(classifyTriangle(200,200,200),'Equilateral','200,200,200 is be equilateral')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

