# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 21:35:37 2021

@author: USER
"""

for i in range(1,20):
    for j in range(1,20):
        if j!=1 and j%2==1:
            print("")
        
        if j%2 == 0:
            print("/ ", end="")
        
        print(str(i) + " * " + str(j) + " = " + str(i*j), end=" ")
        
        if j == 19:
            print("")