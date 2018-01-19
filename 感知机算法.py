# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

感知机算法
Python 3.6

"""

import copy

#输入数据
trainist_set=[[(3,3),1],[(4,3),1],[(1,1),-1]]
w=[0,0]
b=0


#w和b更新
def update(item):
    global w,b
    #w分量的更新
    w[0]=w[0]+1*item[1]*item[0][0]
    w[1]=w[1]+1*item[1]*item[0][1]
    #b分量的更新
    b=b+1*item[1]    
    print("w=",w,",b=",b)

#返回yi(wx+b)的结果    
def judge(item):
    res=0
    for i in range(len(item[0])):
        res=item[0][i]*w[i]  #w*x    
    res=res+b  #w*x+b
    res=res*item[1]  #yi(wx+b)
    return res

#检查数据点是否分对
def check():
    flag=False
    for item in trainist_set:
        if judge(item)<=0:
            flag=True
            update(item)
    return flag

if __name__ == '__main__':
    flag=False
    for i in range(1000):
        if not check():
            flag=True
            break
        
    if flag:
        print("1000 all true")
    else:
        print("something error")
        
        
        
"""
运行结果
runfile('E:/ml/感知机算法.py', wdir='E:/ml')
w= [3, 3] ,b= 1
w= [2, 2] ,b= 0
w= [1, 1] ,b= -1
w= [0, 0] ,b= -2
w= [3, 3] ,b= -1
w= [2, 2] ,b= -2
w= [1, 1] ,b= -3
w= [4, 4] ,b= -2
w= [3, 3] ,b= -3
w= [2, 2] ,b= -4
1000 all true
"""


    
    
    
    
    
    


    

          
    
        
        
    
        







