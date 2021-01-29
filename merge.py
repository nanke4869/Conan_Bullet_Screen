import os
import pandas as pd

df = pd.read_csv('role_count.csv',encoding='gbk')
df = df.fillna(0)
huiyuan_ep = list(df.sort_values(by='小哀', ascending=False).index[:20])
mergefiledir = '柯南'
file = open('txt_all.txt', 'w', encoding='UTF-8')
count = 0
for filename in huiyuan_ep:
    filepath = mergefiledir+'/'+str(filename)+'.txt'
    for line in open(filepath, encoding='UTF-8'):
        file.writelines(line)
    file.write('\n')
    count += 1
    print('第{}集写入完毕'.format(count))
file.close()
