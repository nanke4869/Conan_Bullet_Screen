import jieba
import os
import pandas as pd
os.chdir('D:/pycharm/Conan')
jieba.load_userdict('role.txt')
role = [i.replace('\n', '') for i in open('role.txt', 'r', encoding='utf-8').readlines()]
txt_all = os.listdir('./柯南/')
print(txt_all)
txt_all.sort(key=lambda x: int(x.split('.')[0]))  # 按集数排序
count = 1

df = pd.DataFrame()
for chapter in txt_all:
	names = {}
	data = []
	with open('./柯南/{}'.format(chapter), 'r', encoding='utf-8') as f:
		for line in f.readlines():
			poss = jieba.cut(line)
			for word in poss:
				if word in role:
					if names.get(word) is None:
						names[word] = 0
					names[word] += 1
		df_new = pd.DataFrame.from_dict(names, orient='index', columns=['{}'.format(count)])
		df = pd.concat([df, df_new], axis=1)
	print('第{}集人物统计完毕'.format(count))
	count += 1
df.T.to_csv('role_count.csv', encoding='gb18030')
