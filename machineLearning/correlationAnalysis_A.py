"""
@author: chizi
@software: idea
@file: correlationAnalysis.py
@time: 2022/05/26 23:21
@desc: 机器学习：相关性分析
"""
import pandas as pd
import numpy as np
import sklearn.datasets as skld
import scipy.stats as st
import os

# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# 设置value的显示长度为100，默认为50
pd.set_option('max_colwidth', 300)
path_project = os.path.abspath(os.path.join(os.getcwd(), ".."))
data = pd.read_csv(path_project + '/data/000001.csv')

if __name__ == '__main__':
    data_with_pct_change = pd.DataFrame
    data['close_pct_1d'] = (data['close'] - data['close'].shift(1)) / data['close'].shift(1)
    data['close_pct_3d'] = (data['close'] - data['close'].shift(3)) / data['close'].shift(3)
    data['close_pct_5d'] = (data['close'] - data['close'].shift(5)) / data['close'].shift(5)
    data['close_pct_7d'] = (data['close'] - data['close'].shift(7)) / data['close'].shift(7)
    data['close_pct_9d'] = (data['close'] - data['close'].shift(9)) / data['close'].shift(9)
    data['close_pct_10d'] = (data['close'] - data['close'].shift(10)) / data['close'].shift(10)
    data['close_pct_20d'] = (data['close'] - data['close'].shift(20)) / data['close'].shift(20)
    data['close_pct_30d'] = (data['close'] - data['close'].shift(30)) / data['close'].shift(30)

    # 2 使用pandas中corr()来计算相关性
    coor_pearson = pd.DataFrame(data).corr(method="pearson")
    print(coor_pearson)
    coor_kendall = pd.DataFrame(data).corr(method="kendall")
    print(coor_kendall)
    coor_spearman = pd.DataFrame(data).corr(method="spearman")
    print(coor_spearman)
