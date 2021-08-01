# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 09:37:53 2021

@author: USER
"""

input_data = input()

row = int(input_data[1])
column = ord(input_data[0]) - ord('a') + 1

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

count = 0

for step in steps:
    nx = row + step[0]
    ny = column + step[1]
    
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        count += 1
        
print(count)