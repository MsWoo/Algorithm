# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 11:28:09 2021

@author: USER
"""
def q1():
    global input_str
    temp = input_str[1:] + input_str[0]
    input_str = temp
    print(input_str)
    
def q2():
    global input_str
    temp = input_str[-1] + input_str[0:-1]
    input_str = temp
    print(input_str)
    
def q3():
    global input_str
    temp = input_str[::-1]
    input_str = temp
    print(input_str)
    
    
input_str, q = input().split(" ")
q = int(q)

req = []
for _ in range(q):
    req.append(int(input()))

for i in range(q):
    if req[i] == 1:
        q1()
        
    elif req[i] == 2:
        q2()
        
    else:
        q3()


