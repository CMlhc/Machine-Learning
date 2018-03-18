# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 08:58:16 2018

@author: Lenovo

感知机算法对偶式
Python 3.6

"""

import numpy as np

#构建例子
training_set = np.array([[[3, 3], 1], [[4, 3], 1], [[1, 1], -1]])
#初始化a=0,b=0
a = np.zeros(len(training_set), np.float)
"""
[0. 0. 0.]
"""
b = 0.0
Gram = None
y = np.array(training_set[:, 1])
"""
[1 1 -1]
"""
x = np.empty((len(training_set), 2), np.float)
"""
[[5.56644593e-316 2.06061935e-316]
 [5.56396375e-316 2.06061935e-316]
 [5.56645226e-316 2.06062172e-316]]
"""
for i in range(len(training_set)):
    x[i] = training_set[i][0]


#构建Gram矩阵
def cal_gram():
    g = np.empty((len(training_set), len(training_set)), np.int)
    for i in range(len(training_set)):
        for j in range(len(training_set)):
            g[i][j] = np.dot(training_set[i][0], training_set[j][0])
    return g


#更新数据
def update(i):
    global a, b
    a[i] += 1   #ai=ai+1
    b = b + y[i]  #bi=b+yi*1
    print(a,b)


#误分条件
def cal(i):
    global a, b, x, y
    res = np.dot(a * y, Gram[i])
    res = (res + b) * y[i]
    return res

#检查是否分类成功
def check():
    global a, b, x, y
    flag = False
    for i in range(len(training_set)):
        if cal(i) <= 0:
            flag = True
            update(i)
    if not flag:
        w = np.dot(a * y, x)
        print("RESULT: w: " + str(w) + " b: " + str(b))
        return False
    return True


if __name__ == "__main__":
    Gram = cal_gram() 
    for i in range(1000):
        if not check(): break
    
  
"""
运行结果
runfile('E:/ml/2 感知机算法对偶式.py', wdir='E:/ml')
[1. 0. 0.] 1.0
[1. 0. 1.] 0.0
[1. 0. 2.] -1.0
[1. 0. 3.] -2.0
[2. 0. 3.] -1.0
[2. 0. 4.] -2.0
[2. 0. 5.] -3.0
RESULT: w: [1.0 1.0] b: -3.0
"""
