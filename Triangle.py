# -*- coding: utf-8 -*-
"""
Created on Thu Feb 4 21:30:00 2020
Updated Feb 4, 2020

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: rzhong2
"""

def classifyTriangle(a,b,c):
    """
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <=0  or c <= 0:
        return 'InvalidInput'
    

    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if a<b+c and b<a+c and c<a+b:
        if a==b==c:
            return('Equilateral')
        elif a==b or a==c or b==c:
            return('Isoceles')
        elif a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
            return('Right')
        else:
            return('Scalene')
    else:
        return('NotATriangle')