# knn简单实现
import operator

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
def KNNClassify(newInput, X_train, Y_train, k, weight):
    # newInput: 新输入的待分类数据(x_test)，本分类器一次只能对一个新输入分类
    # dataset：输入的训练数据集(x_train),array类型，每一行为一个输入训练集
    # labels：输入训练集对应的类别标签(y_train)，格式为['A','B']而不是[['A'],['B']]
    # k：近邻数
    # weight：决策规则，"uniform" 多数表决法，"distance" 距离加权表决法

    numSamples = X_train.shape[0]

    """step1: 计算待分类数据与训练集各数据点的距离（欧氏距离：距离差值平方和开根号）"""
    diff = np.tile(newInput, (numSamples, 1)) - X_train  # np.tile作用是复制。将newInput沿第1个维度复制numSamples次
    squaredist = diff ** 2
    distance = (squaredist.sum(axis=1)) ** 0.5  # axis=1,沿第1个维度相加（即行）
    # print(squaredist[:5])
    #
    # np.set_printoptions(suppress=True)
    # print(squaredist[:5])
    # print(distance[:5])
    # exit()

    """step2：将距离按升序排序，并取距离最近的k个近邻点"""
    # 对数组distance按升序排序，返回数组排序后的值对应的索引值
    sortedDistance = distance.argsort()
    # print(sortedDistance)
    # print(distance[sortedDistance[:5]])
    # exit()

    # 定义一个空字典，存放k个近邻点的分类计数
    classCount = {}

    # 对k个近邻点分类计数，多数表决法
    for i in range(k):
        # 第i个近邻点在distance数组中的索引,对应的分类
        votelabel = Y_train[sortedDistance[i]]
        if weight == "uniform":
            # votelabel作为字典的key，对相同的key值累加（多数表决法）
            classCount[votelabel] = classCount.get(votelabel, 0) + 1
        elif weight == "distance":
            # 对相同的key值按距离加权累加（加权表决法）
            classCount[votelabel] = classCount.get(votelabel, 0) + (1 / distance[sortedDistance[i]])
        else:
            print("分类决策规则错误！")
            print("\"uniform\"多数表决法\"distance\"距离加权表决法")
            break

            # 对k个近邻点的分类计数按降序排序，返回得票数最多的分类结果
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    # print(sortedClassCount)
    # print(classCount.items())
    # exit()
    if weight == "uniform":
        print("新输入到训练集的最近%d个点的计数为：" % k, "\n", classCount)
        print("新输入的类别是:", sortedClassCount[0][0])

    elif weight == "distance":
        print("新输入到训练集的最近%d个点的距离加权计数为：" % k, "\n", classCount)
        print("新输入的类别是:", sortedClassCount[0][0])

    return sortedClassCount[0][0]

data = load_iris()
X = data['data']
Y = data['target']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

test_id = 2
test_pred = KNNClassify(X_test[test_id], X_train, Y_train, 3, 'uniform')

