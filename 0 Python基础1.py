# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 22:40:46 2018

@author: Lenovo
Python 3.6

"""

#字典

d={'cat':'cute','dog':'furry'}
print(d['cat'])
print('cat' in d)
d['fish']='wet' #增加一个新的字典
print(d['fish'])

print(d.get('monkey','N/A'))
print(d.get('fish','N/A'))
del(d['fish'])  #把这个键值删除
print(d.get('fish','N/A'))
print('--------------')
"""
cute
True
wet
N/A
wet
N/A
"""

#循环Loops

d={'person':2,'cat':4,'spider':8}
for animal in d:
    legs=d[animal]
    print(animal," has ",legs," legs")
print('----------------')
"""
person  has  2  legs
cat  has  4  legs
spider  has  8  legs
"""

    

"""    
#如果要访问对于的键和值
for animal,legs in d.items:
    print(animal," has ",legs," legs")
"""  


#字典序的推导
nums=[0,1,2,3,4]
even_num_to_square={x:x**2 for x in nums if x%2==0}
print(even_num_to_square)
print('-------------')
"""
{0: 0, 2: 4, 4: 16}
"""


#集合Sets
#独立不同个体的集合
animal={'cat','dog'}
print('cat' in animal)
print('fish' in animal)
animal.add('fish')
print('fish' in animal)
print(len(animal))
animal.add('cat')
print(len(animal))
animal.remove('cat')
print(len(animal))
print('------------')
"""
True
False
True
3
3
2
"""
animals={'cat','dog','fish'}
for idx,aniaml in enumerate(animals):
    print(idx+1," : ",animal)
    
from math import sqrt
nums={int(sqrt(x)) for x in range(32)}
print(nums)
print('----------')
"""
1  :  {'dog', 'fish'}
2  :  {'dog', 'fish'}
3  :  {'dog', 'fish'}
{0, 1, 2, 3, 4, 5}
"""

#元组Tuples
#是一个有序的列表，且不可改变
d = {(x, x + 1): x for x in range(10)}  
print(d)
t = (5, 6)       
print(type(t))    
print(d[t])       
print(d[(1, 2)])
print('---------------') 
"""
{(0, 1): 0, (1, 2): 1, (2, 3): 2, (3, 4): 3, (4, 5): 4, (5, 6): 5, (6, 7): 6, (7, 8): 7, (8, 9): 8, (9, 10): 9}
<class 'tuple'>
5
1
"""


#函数
def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

for x in [-1, 0, 1]:
    print(sign(x))
print('------------')
"""
negative
zero
positive
"""

def hello(name, loud=False):
    if loud:
        print('HELLO, %s' % name.upper())
    else:
        print('Hello, %s!' % name)

hello('Bob') 
hello('Fred', loud=True)  
print('------------')
"""
Hello, Bob!
HELLO, FRED
"""


#类的定义
class Greeter(object):
    def __init__(self, name):
        self.name = name 
    def greet(self, loud=False):
        if loud:
            print('HELLO, %s!' % self.name.upper())
        else:
            print('Hello, %s' % self.name)

g = Greeter('Fred')  
g.greet()           
g.greet(loud=True) 
print('---------')
"""
Hello, Fred
HELLO, FRED!
"""


