# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 09:23:32 2021

@author: USER
"""

n = int(input())
data = list(input().split())

x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for d in data:
    for i in range(len(move)):
        if d == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        
        x, y = nx, ny

print(x, y)