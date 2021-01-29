import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plt.rcParams['font.sans-serif'] = ['kaiti']
plt.style.use('ggplot')
df = pd.read_csv('role_count.csv', encoding='gbk')
df = df.fillna(0)  # 空缺处补0
df = df.drop([df.columns[0]], axis=1)  # 把第一列的序号删掉
plt.figure(figsize=(20, 10))
role_sum = df.sum().to_frame().sort_values(by=0, ascending=False)
g = sns.barplot(role_sum.index, role_sum[0], palette='Set3', alpha=0.8)
index = np.arange(len(role_sum))
for name, count in zip(index, role_sum[0]):
    g.text(name, count+50, int(count), ha='center', va='bottom',)
plt.title('B站名侦探柯南弹幕——主要人物讨论总次数分布')
plt.ylabel('讨论次数')
plt.savefig("B站名侦探柯南弹幕——主要人物讨论总次数分布")
plt.show()