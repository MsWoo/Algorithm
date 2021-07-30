# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 19:25:23 2021

@author: USER
"""

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 #그룹
count = 0 #현재그룹에 포함된 모험가의수

#i는 공포도
for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)