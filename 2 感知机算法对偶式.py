# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 08:58:16 2018

@author: Lenovo

感知机算法对偶式
Python 2.7
#无法运行
File "E:/ml/感知机算法对偶式.py", line 36, in cal_gram
TypeError: 'numpy.int32' object does not support item assignment
"""

import numpy as np
training_set=np.array([[[3,3],1],[[4,3],1],[[1,1],-1]])

a=np.zeros(len(training_set),np.float)
b=0.0
Gram=None
#print(len(training_set))

y=np.array(training_set[:,1])
#print(y)

x=np.empty((len(training_set),2),np.float)
#print(x)

for i in range(len(training_set)):
    x[i]=training_set[i][0]

#print(x)

#构建gram矩阵
def cal_gram():
    g=np.array((len(training_set),len(training_set)),np.int)
    
    for i in range(len(training_set)):
        for j in range(len(training_set)):
            g[i][j]=np.dot(training_set[i][0],training_set[j][0])
    return g

def update(i):
    global a,b
    a[i]=a[i]+1
    b=b+y[i]
    print(a,b)


def cal(i):
    global a,b,x,y
    res=np.dot(a*y,Gram[i])
    res=(res+b)*y[i]
    return res

def check():
    global a,b,x,y
    flag=False
    for i in range(len(training_set)):
        if cal(i)<=0:
            flag=True
            update(i)
    if not flag:
        w=np.dot(a*y,x)
        print  "RESULT: w: " + str(w) + " b: " + str(b)
        return False
    return True


if __name__ == "__main__":
    Gram = cal_gram()  
    for i in range(1000):
        if not check(): break
        
    
