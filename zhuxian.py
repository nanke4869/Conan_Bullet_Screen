import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('role_count.csv', encoding='gbk')
df = df.fillna(0)  # 空缺处补0

plt.rcParams['font.sans-serif'] = ['kaiti']
plt.style.use('ggplot')
plt.figure(figsize=(20, 10))
names = ['琴酒', '伏特加', '贝姐']
colors = ['#090707', '#004e66', '#EC7357']
alphas = [0.8, 0.7, 0.6]
for name, color, alpha in zip(names, colors, alphas):
    plt.plot(df.index, df[name], label=name, color=color, alpha=alpha)
plt.legend(loc='best',frameon=False)
plt.annotate('集数:{},讨论次数:{}'.
             format(df['琴酒'].idxmax() + 1, int(df['琴酒'].max())),
             xy=(df['琴酒'].idxmax(), df['琴酒'].max()),
             xytext=(df['琴酒'].idxmax()+30, df['琴酒'].max()),
             arrowprops=dict(color='red', headwidth=8, headlength=8)
            )
plt.xlabel('集数')
plt.ylabel('讨论次数')
plt.title('酒厂成员讨论次数分布图')
plt.hlines(xmin=df.index.min(), xmax=df.index.max(), y=200, linestyles='--', colors='red')
# plt.ylim(0, 800)
plt.savefig("酒厂成员讨论次数分布图")
plt.show()

# 输出主线剧集
mainline = set(list(df[df['贝姐'] >= 200].index)+list(df[df['琴酒'] >= 200].index))  # 伏特加可忽略不计
print(mainline)
