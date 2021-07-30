# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 19:04:39 2021

@author: USER
"""

n = 1260
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count += n // coin
    n %= coin
    
print(count)

#화폐의종류가 K개라면 O(K)의 시간복잡도.

