# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 09:31:56 2021

@author: USER
"""

n = int(input())
count = 0

for i in range(0, n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)