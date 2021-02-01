# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:44:45 2021

@author: WangFen
"""


import pandas as pd

# 导入数据
result = pd.read_csv("car_complain.csv")

# 数据预处理
# 拆分problem类型
result = result.drop("problem", axis = 1).join(result.problem.str.get_dummies(','))

# 数据清洗，合并名称
def f(x):
    x = x.replace("一汽-大众","一汽大众")
    return x

# 品牌投诉总数
print("品牌投诉总数，从大到小排序:")
result['brand'] = result['brand'].apply(f)
df = result.groupby(['brand'])['id'].agg(['count']).sort_values('count', ascending = False)
df.reset_index(inplace=True)
print(df)
print("====================================")

# 车型投诉总数
print("车型投诉总数，从大到小排序:")
df1 = result.groupby(['car_model'])['id'].agg(['count']).sort_values('count', ascending = False)
df1.reset_index(inplace=True)
print(df1)
print("====================================")

# 品牌的平均车型投诉
print("品牌的平均车型投诉，从大到小排序:")
df2 = result.groupby(['brand','car_model'])['id'].agg(['count'])
df2.reset_index(inplace=True)
# print(df2)
df2 = df2.groupby(['brand']).mean().sort_values('count', ascending = False)
df2.reset_index(inplace=True)
print(df2)