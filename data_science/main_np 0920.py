import numpy as np

print("-------------读取数据--------------")
# 读取数据
salaries = np.genfromtxt('data/salaries.txt', delimiter=",", dtype=str)
# print(help(numpy.genfromtxt))
# print('数据类型：', type(salaries))
# print('数据详情：\n', salaries)

# # 去掉第一行表头
# salaries1 = np.genfromtxt('salaries.txt', delimiter=",", dtype=str, skip_header=1)
# print('数据详情1：\n', salaries1)
#
# print("-------------数据概况--------------")
# # 查看数据概况
# # 数据量大小：行数、列数
# print('行数：', salaries.shape[0])
# print('列数：', salaries.shape[1])
# print('数据量大小:', salaries.shape)
#
# print("-------------数据详情--------------")
# # 查看部分数据
# print('第11行第6个数据：\n', salaries[10,5])
# print('前5行数据：\n', salaries[:5,:])
# # 练习： 查看倒数第二列的数据
# # print(salaries[:,-2])
#
# # 练习： 如何去掉表头，将剩余的数据内容保留，并验证
# # salaries1 = salaries[1:,:]
# # print(salaries1.shape)
# # print(salaries1)

# 数据分析
# print("-------------简单的数据探索--------------")
# print("-------对属性的探索-------")
# # rank列共有哪些取值，以及每个值出现的个数
# rank = salaries[1:, 1]
# from collections import Counter
# print(Counter(rank))

# salaries = salaries[1:,:]
# discipline = salaries[:,2]
# print(Counter(discipline))
#
# sex = salaries[:,-2]
# print(Counter(sex))
#
# yr_phd = salaries[:,-4]
# print('新进老师人数：', sum(yr_phd=='1'))
#
# # print('新进老师人数：', sum(yr_phd < 3))
# # 更改数据存储格式
# print(yr_phd.dtype)
# yr_phd = yr_phd.astype('float')
# print(yr_phd.dtype)
# print('新进老师人数：', sum(yr_phd < 3))
#
