# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 19:06:32 2021

@author: USER
"""

n, k = map(int, input().split())

result = 0

while True:
    target = (n//k) * k
    result += (n - target)
    n = target
    
    if n<k:
        break
    
    result += 1
    n //= k

result += (n - 1)
print(result)
