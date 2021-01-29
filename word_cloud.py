# -*-coding:utf-8-*-
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

stopwords = [line.strip() for line in open('Library/stopwords.txt', 'r', encoding='utf-8')]
with open('柯南/547.txt', 'r', encoding='utf-8') as f:
    txt = f.read()
    words = jieba.cut(txt)
    sentences = ""
    for word in words:
        if word in stopwords:
            continue
        sentences += str(word)+' '
    wordcloud = WordCloud(background_color='white',
                          font_path="Library/SourceHanSerif-Heavy.ttc",
                          width=2000,
                          height=2000,).generate(sentences)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.savefig("547集琴酒词云")
    plt.show()