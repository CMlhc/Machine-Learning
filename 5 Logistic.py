# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 08:10:44 2018

@author: Lenovo
Python 2.7
"""

# 项目案例1: 使用 Logistic 回归在简单数据集上的分类
from numpy import *


#解析数据
def loadDataSet(file_name):
    dataMat=[]
    labelMat=[]
    fr=open(file_name)
    for line in fr.readlines():
        lineArr=line.strip().split()
        # 为了方便计算，我们将 X0 的值设为 1.0 ，也就是在每一行的开头添加一个 1.0 作为 X0
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat



#sigmoid跳跃函数
def sigmoid(inX):
    return 1.0/(1+exp(-inX))



#正常的梯度上升法
def gradAscent(dataMatIn,classLabels):
    #将其转化为numpy矩阵
    dataMatrix=mat(dataMatIn)
    #将行向量转化为列向量
    labelMat=mat(classLabels).transpose()
    #获取数据量和样本数
    m,n=shape(dataMatrix)
    
    #确定移动步长
    alpha=0.001
    #确定迭代次数
    maxCycles=500
    #确定回归系数
    weights=ones((n,1))
    for k in range(maxCycles):
        #矩阵乘法
        h = sigmoid(dataMatrix*weights)
        #albelMat是实际值
        error=(labelMat - h)
        weights = weights + alpha * dataMatrix.transpose() * error # 矩阵乘法，最后得到回归系数
    return array(weights)


#梯度上升算法
def stocGradAscent(dataMatrix,classLabels,numIter=150):
    m,n=shape(dataMatrix)
    weights=ones(n)
    
    #随机梯度，循环150，判断是否收敛
    for j in range(numIter):
        dataIndex=range(m)
        for i in range(m):
            #i 和 j 不断的扩大，导致alpha的值不断的减少，但不为0
            alpha=4/(1.0+j+i)+0.001
            #随机产生一个数
            randIndex=int(random.uniform(0,len(dataIndex)))
            h = sigmoid(sum(dataMatrix[randIndex]*weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex]
            del(dataIndex[randIndex])
    return weights   



#简单的尝试
def simpleTest():
    dataMat,labelMat=loadDataSet("testSet.txt")
    dataArr=array(dataMat)
    weights=stocGradAscent(dataArr,labelMat)
      
            
    
    
    
    
    
    
    
    
    

#从疝气病症预测病马的死亡率

#分类函数，根据回归系数和特征向量来计算 sigmoid 的值
def classifyVector(inX,weights):
    prob=sigmoid(sum(inX*weights))
    if prob >0.5:
        return 1.0
    else:
        return 0.0



#打开训练集和测试集，并对数据进行处理
def colicTest():
    frTrain=open('horseColicTraining.txt')
    frTest=open('horseColicTest.txt')
    trainingSet=[]
    trainingLabels=[]
    
    #解析数据和Labels
    for line in frTrain.readlines():
        currLine=line.strip().split('\t')
        lineArr=[]
        for i in range(21):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[21]))
        
    # 使用 改进后的 随机梯度下降算法 求得在此数据集上的最佳回归系数 trainWeights
    trainWeights = stocGradAscent(array(trainingSet), trainingLabels, 500)
    errorCount = 0
    numTestVec = 0.0
    # 读取 测试数据集 进行测试，计算分类错误的样本条数和最终的错误率
    for line in frTest.readlines():
        numTestVec += 1.0
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        if int(classifyVector(array(lineArr), trainWeights)) != int(currLine[21]):
            errorCount += 1
    errorRate = (float(errorCount) / numTestVec)
    print "the error rate of this test is: %f" % errorRate
    return errorRate



#调用10次 colicTest 并求平均值
def multiTest():
    numTests=10
    errorSum=0.0
    for k in range(numTests):
        errorSum += colicTest()
    print "after %d iterations the average error rate is: %f" % (numTests, errorSum/float(numTests)) 
    
    
    




if __name__ == "__main__":
    #simpleTest()
    multiTest()
