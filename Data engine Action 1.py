

# nr. 1:  2,4,...100 求和
import numpy as np

x1 = np.arange(2, 101, 2)
print("总和为")
print(np.sum(x1))

# nr. 2 成绩统计

import numpy as np
from pandas import Series, DataFrame

persontype = np.dtype({
    'names': ['name', 'chinese', 'math', 'english'],
    'formats': ['S32', 'i', 'i', 'i']})
peoples = np.array([("ZhangFei", 68, 65, 30), ("GuanYu", 95, 76, 98), ("Liu Bei", 98, 86, 88), ("dian wei", 90, 88, 77),
                    ("xu zhe", 80, 98, 90)], dtype=persontype)


df1 = DataFrame(peoples)
print(df1)

print("   \n 个人成绩统计  ")
for i in range(5):
    sum_ = df1.iloc[i, 1:].sum()
    min_ = df1.iloc[i, 1:].min()
    max_ = df1.iloc[i, 1:].max()
    mean_ = df1.iloc[i, 1:].mean()
    var_ = df1.iloc[i, 1:].var()
    std_ = df1.iloc[i, 1:].std()

    print(df1.iloc[i]['name'])
    print("总分："+ str(sum_)+"\n最高分："+ str(max_)+"\n最低分："+ str(min_)+"\n平均分："+str(mean_))

print("   \n 各科成绩统计  ")
for i in range (3):
    sum1 = df1.iloc[:,i+1].sum()
    min1 = df1.iloc[:,i+1].min()
    max1 = df1.iloc[:,i+1].max()
    mean1 = df1.iloc[:,i+1].mean()
    var1 = df1.iloc[:,i+1].var()
    std1 = df1.iloc[:,i+1].std()

    if i==0:
        print ("语文")
        print("总分：" + str(sum1) + "\n最高分：" + str(max1) + "\n最低分：" + str(min1) + "\n平均分：" + str(mean1)+"\n方差："+str(var1)+"\n标准差："+str(std1))
    if i==1:
        print("\n数学")
        print("总分：" + str(sum1) + "\n最高分：" + str(max1) + "\n最低分：" + str(min1) + "\n平均分：" + str(mean1) + "\n方差：" + str(
            var1) + "\n标准差：" + str(std1))
    if i == 2:
        print("\n英语")
        print("总分：" + str(sum1) + "\n最高分：" + str(max1) + "\n最低分：" + str(min1) + "\n平均分：" + str(mean1) + "\n方差：" + str(
            var1) + "\n标准差：" + str(std1))

# 总成绩排序
total = {}
for i in range(len(peoples)):	total[peoples[i][0]] = peoples[i][1] + peoples[i][2] + peoples[i][3]

total = sorted(total.items(), key = lambda x: x[1], reverse = True)
print('\n总成绩排序：')
for i in range(len(total)):
    print("第{}名： {}\t总成绩： {}".format(i+1, total[i][0], total[i][1]))

