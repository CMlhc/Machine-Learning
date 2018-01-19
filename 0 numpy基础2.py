# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 14:21:58 2018

@author: Lenovo
"""

import numpy as np

#计算A**2+B**3.A,B是一维数组

def pySum():
    a=[0,1,2,3,4]
    b=[9,8,7,6,5]
    c=[]
    
    for i in range(len(a)):
        c.append(a[i]**2+b[i]**3)
    return c

print(pySum())
"""
[729, 513, 347, 225, 141]
"""
def npSum():
    a=np.array([0,1,2,3,4])
    b=np.array([9,8,7,6,5])
    
    c=a**2+b**3
    return c

print(npSum())
"""
[729 513 347 225 141]
"""


a=np.array([[0,1,2,3,4],[9,8,7,6,5]])
print(a)
"""
[[0 1 2 3 4]
 [9 8 7 6 5]]
"""

#秩
print(a.ndim)
"""
2
"""

#n行m列
print(a.shape)
"""
(2, 5)
"""

#元素的个数，相当于n*m
print(a.size)
"""
10
"""

#元素的类型
print(a.dtype)
"""
int32
"""

#每个元素的大小，以字节为单位
print(a.itemsize)
"""
4
"""



