# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 20:50:28 2021

@author: USER
"""

def fac_iterative(n):
    result = 1
    
    for i in range(1, n+1):
        result *= i
    return result

def fac_recursive(n):
    if n <= 1:
        return 1
    return n * fac_recursive(n-1)

print(fac_iterative(5))
print(fac_recursive(5))