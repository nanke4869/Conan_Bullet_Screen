# -*-coding:utf-8-*-

import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['kaiti']
plt.style.use('ggplot')

df = pd.read_csv('role_count.csv', encoding='gbk')
df = df.fillna(0)
xinyi = df[df['新一'] >= 250]['新一'].to_frame()
print(xinyi)  # 新一登场集数

plt.figure(figsize=(20, 10))
plt.plot(df.index, df['新一'], label='新一', color='blue', alpha=0.6)
plt.annotate('集数:50,讨论次数:439',
             xy=(50, 439),
             xytext=(40, 420),
             arrowprops=dict(color='red', headwidth=8, headlength=8)
            )
plt.annotate('集数:235,讨论次数:392',
             xy=(235, 392),
             xytext=(225, 370),
             arrowprops=dict(color='red', headwidth=8, headlength=8)
            )
plt.annotate('集数:572,讨论次数:504',
             xy=(572, 504),
             xytext=(563, 480),
             arrowprops=dict(color='red', headwidth=8, headlength=8)
            )
plt.annotate('集数:825,讨论次数:307',
             xy=(825, 307),
             xytext=(815, 280),
             arrowprops=dict(color='red', headwidth=8, headlength=8)
            )
plt.hlines(xmin=df.index.min(), xmax=df.index.max(), y=250, linestyles='--', colors='red')
plt.legend(loc='best', frameon=False)
plt.xlabel('集数')
plt.ylabel('讨论次数')
plt.title('工藤新一讨论次数分布图')
plt.savefig("工藤新一讨论次数分布图")
plt.show()
