# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:23:51 2021

@author: USER
"""

def gcd(a, b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)
    
print(gcd(192,162))