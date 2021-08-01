# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 09:57:19 2021

@author: USER
"""

S = input()

inputs = []
sum = 0

for i in S:
    if i.isalpha():
        inputs.append(i)
    else:
        sum += int(i)
        
inputs.sort()

if sum != 0:
    inputs.append(str(sum))
    
print(''.join(inputs))