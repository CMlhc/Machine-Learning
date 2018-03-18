# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 18:36:47 2018

@author: Lenovo
Python 3.6
来自《机器学习实战》第二章 K近邻算法

"""

from numpy import *
import operator
from os import listdir
from collections import Counter

#创建数据集和标签
def createDataSet():
    group=array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    
    return group,labels

#kNN原始算法
def classify0(inX,dataSet,labels,k):
    """
    inx：分类的向量
    dataSet：训练样本
    labels：标签向量
    k：选择最临近的项目
    """
    dataSetSize=dataSet.shape[0] #训练样本的个数
    diffMat=tile(inX,(dataSetSize,1))-dataSet  #需要分类的向量到各个点的直线距离
    
    #取平方
    sqDiffMat=diffMat**2
    #将矩阵的每一行相加，由二维矩阵变成一维矩阵
    sqDistances=sqDiffMat.sum(axis=1)
    #开方
    distances=sqDistances**0.5
    #距离进行从小到大排序
    sortdistances=distances.argsort()
    classCount={}
    for i in range(k):
        #获取距离的第i个标签
        notelabels=labels[sortdistances[i]]
        
        #对该标签的值进行累加
        classCount[notelabels]=classCount.get(notelabels,0)+1 
        # 在字典中将该类型加一
        # 字典的get方法
        # 如：list.get(k,d) 其中 get相当于一条if...else...语句,参数k在字典中，字典将返回list[k];如果参数k不在字典中则返回参数d,如果K在字典中则返回k对应的value值
        # l = {5:2,3:4}
        # print l.get(3,0)返回的值是4；
        # Print l.get（1,0）返回值是0；
        
        
        #对所出现的标签进行排序
        sortedclassCount=sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
        # 3. 排序并返回出现最多的那个类型
        # 字典的 items() 方法，以列表返回可遍历的(键，值)元组数组。
        # 例如：dict = {'Name': 'Zara', 'Age': 7}   print "Value : %s" %  dict.items()   Value : [('Age', 7), ('Name', 'Zara')]
        # sorted 中的第2个参数 key=operator.itemgetter(1) 这个参数的意思是先比较第几个元素
        # 例如：a=[('b',2),('a',1),('c',0)]  b=sorted(a,key=operator.itemgetter(1)) >>>b=[('c',0),('a',1),('b',2)] 可以看到排序是按照后边的0,1,2进行排序的，而不是a,b,c
        # b=sorted(a,key=operator.itemgetter(0)) >>>b=[('a',1),('b',2),('c',0)] 这次比较的是前边的a,b,c而不是0,1,2
        # b=sorted(a,key=opertator.itemgetter(1,0)) >>>b=[('c',0),('a',1),('b',2)] 这个是先比较第2个元素，然后对第一个元素进行排序，形成多级排序。
        #返回最大可能的这一个
        return sortedclassCount[0][0]
    
    
#对第一个例子进行演示
def test1():
    group,labels=createDataSet()
    print(str(group))
    print(str(labels))
    print(classify0([0.1,0.1],group,labels,3))
    
"""
运行结果
runfile('E:/ml/2 KNN.py', wdir='E:/ml')
[[ 1.   1.1]
 [ 1.   1. ]
 [ 0.   0. ]
 [ 0.   0.1]]
['A', 'A', 'B', 'B']
B
"""


#文件处理
def file2matrix(filename):
    #打开文件
    fr=open(filename)
    #获取文件数据中的行数
    numberOFlines=len(fr.readlines())
    #生成对应的空矩阵
    returnMat=zeros((numberOFlines,3))
    
    classlabelVector=[]
    fr=open(filename)
    index=0
    #对每一行进行处理
    for line in fr.readlines():
        #移除首尾字符的空格
        line=line.strip()
        #将字符串的空格进行切片
        listFROMline=line.split('\t')
        #将每列的属性数据放入矩阵
        returnMat[index,:]=listFROMline[0:3]
        #将每类的标签数据放入标签容器
        classlabelVector.append(int(listFROMline[-1]))
        index=index+1        
    return returnMat,classlabelVector


#归一化数据
def aotoNorm(dataSet):
    #计算每种属性的最大值，最小值，范围
    minVals=dataSet.min(0)
    maxVals=dataSet.max(0)
    #极差
    ranges=maxVals-minVals
    
    """
    归一化公式
        Y = (X - minx)/( maxx - minx)
    """
    normDataset=(dataSet-minVals)/ranges
    return normDataset,ranges,minVals



#对约会网站进行测试
def datingClassTest():
    #设置测试的比例
    hoRatio=0.1
    #从文件中加载数据
    DataMat,Labels=file2matrix('datingTestSet2.txt')
    #归一化数据
    normDataSet,ranges,minVals=aotoNorm(DataMat)
    #m表示数据的行数 
    m=normDataSet.shape[0]
    #设置测试样本数量
    numTextVecs=int(m*hoRatio)
    print("numTestVecs= ",numTextVecs)
    
    #设置错误率
    errorCount=0.0
    
    for i in range(numTextVecs):
        #对测试数据
        classifierResult = classify0(normDataSet[i, :], normDataSet[numTextVecs:m, :], Labels[numTextVecs:m], 3)
        print("the classifier came back with:  ",classifierResult," the real answer is: ", Labels[i])
        if (classifierResult != Labels[i]): errorCount += 1.0
    print("the total error rate is: " ,errorCount / float(numTextVecs))
    print(errorCount)
    
    
#将图像数据转化为向量
def img2vector(filename):
    """
    因为输入的图片的格式是32*32，所以用1*1024个数组
    """
    returnVect=zeros((1,1024))
    fr=open(filename)
    for i in range(32):
        line=fr.readline()
        """
        readline每次读取一行，返回的是一个字符串对象
        readlines一次性读取整个文件，自动将文件内容分析成一个行列表
        """
        for j in range(32):
            returnVect[0,32*i+j]=line[j]
    return returnVect


#手写数据识别
def handwritingClassTest():
    hwLabels = []
    #载入训练集
    trainingFileList=listdir('trainingDigits')
    #数据的个数
    m=len(trainingFileList)
    trainingMat=zeros((m,1024))
    #Labels存贮0-9对应的index的位置，trainingMat存放每个位置对应的图片向量
    for i in range(m):
        #把每个文件名读取为字符串，并对字符串进行分解，提取标签
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]  # take off .txt
        classNumStr = int(fileStr.split('_')[0])
        #将标签放入数组
        hwLabels.append(classNumStr)
        # 将 32*32的矩阵->1*1024的矩阵
        trainingMat[i, :] = img2vector('trainingDigits/%s' % fileNameStr)

    # 导入测试数据
    testFileList = listdir('testDigits')  # iterate through the test set
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]  # take off .txt
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print("the classifier came back with: ",classifierResult,"the real answer is:  " , classNumStr)
        if (classifierResult != classNumStr): errorCount += 1.0
    
    
    print("\nthe total number of errors is: " , errorCount)
    print("\nthe total error rate is: ",errorCount / float(mTest))

        
    
    
    

    
    
    
if __name__ == '__main__':
    test1()
    datingClassTest()
    handwritingClassTest()
    
    
    
    
  

