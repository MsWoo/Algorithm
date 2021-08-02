# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 20:37:54 2021

@author: USER
"""
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(1)
queue.pop()
queue.popleft()


print(queue)
queue.reverse()
print(queue)