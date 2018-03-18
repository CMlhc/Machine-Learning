# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 21:33:59 2018

@author: Lenovo
Python 3.6
"""


###基本数据类型

#数字
x = 3
print(type(x))
print(x)
print(x+1)
print(x-1)
print(x*2)
print(x**2)
print('-----------')
"""
runfile('E:/ml/0 Python基础.py', wdir='E:/ml')
<class 'int'>
3
4
2
6
9
"""

x +=1
print(x)
x *=2
print(x)
y = 2.5
print(type(y))
print(y,y+1,y * 2,y ** 2)
print('-------------')
"""
4
8
<class 'float'>
2.5 3.5 5.0 6.25
"""

#布尔型
t=True
f=False
print(type(t))
print(t and f)
print(t or f)
print(not f)
print(t != f)
print('------------')
"""
<class 'bool'>
False
True
True
True
"""

#字符串
hello='hello'
world="world"
print(hello)
print(len(hello))
hw=hello+ ' ' +world  #将字符串进行连接
print(hw)
hw12=hello+' '+world+' '+'12'
print(hw12)
print('-------------')
"""
hello
5
hello world
hello world 12
"""

#对字符串的一些使用
s = 'hello'
print(s.capitalize)
print(s.upper)
print(s.rjust(7))
print(s.center(7))
print(s.replace('l','(ell)'))

print('  world   '.strip)
print('-------------')
"""
<built-in method capitalize of str object at 0x00000275FB7A3FB8>
<built-in method upper of str object at 0x00000275FB7A3FB8>
  hello
 hello 
he(ell)(ell)o
<built-in method strip of str object at 0x00000275FB7C4470>
"""

###容器

#列表List
"""
列表表示Python中的数组，但列表的长度可变，且包含不同元素类型元素
"""

xs=[3,1,2]  #创建列表
print(xs,xs[2])
print(xs[-1]) 
xs[2]='foo'
print(xs)
xs.append('bar')
print(xs)
x=xs.pop() #将队尾的元素取出
print(x,xs)
print('-------------')
"""
[3, 1, 2] 2
2
[3, 1, 'foo']
[3, 1, 'foo', 'bar']
bar [3, 1, 'foo']
"""

#切片Slicing
nums=range(5)
print(nums)
print(nums[2:4])
print(nums[2:])
print(nums[:2])
print(nums[:])
print(nums[:-1])
#nums[2:4]=[8,9]
print(nums)
print('--------------')
"""
range(0, 5)
range(2, 4)
range(2, 5)
range(0, 2)
range(0, 5)
range(0, 4)
range(0, 5)
"""


#循环Loops
animals = ['cat','dog','monkey']
for animal in animals:
    print(animal)
print('--------------')
"""
cat
dog
monkey
"""

#在循环内访问每个元素的指针
for idx,animal in enumerate(animals):
    print('#',idx,':',animal)
print('--------------')
"""
# 0 : cat
# 1 : dog
# 2 : monkey
"""

#将列表中的元素变成它的平方
nums=[0,1,2,3,4]
squares=[]
for x in nums:
    squares.append(x**2)
print(squares)
print('--------------')
"""
[0, 1, 4, 9, 16]
"""

#利用列表推导
nums=[0,1,2,3,4]
squares=[x**2 for x in nums]
print(squares)
print('--------------')
"""
[0, 1, 4, 9, 16]
"""

#列表推导还可以包括条件
nums=[0,1,2,3,4]
squares=[x**2 for x in nums if x%2==0]
print(squares)
print('-----------------')
"""
[0, 4, 16]
"""

