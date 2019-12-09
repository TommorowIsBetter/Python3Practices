#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:Wang Yan
@ide:PyCharm
@time:2019/12/4 15:23
"""
import math
import jieba
import nltk
def entropy(labels):
    # 计算信息熵
    freqdist = nltk.FreqDist(labels)
    probs = [freqdist.freq(l) for l in freqdist]
    return -sum(p * math.log(p, 2) for p in probs)


def seg_depart_del_stop_words_list(sentence):
    # 对文本进行分词
    stopwords = [line_.strip() for line_ in open('stopwords.txt', encoding='UTF-8').readlines()]
    # 进行结巴分词
    sentence_depart = jieba.cut(sentence.strip())
    # 创建一个停用词列表
    out_list = []
    # 去停用词
    for word in sentence_depart:
        if word not in stopwords:
            if word != '\t':
                out_list.append(word)
    return out_list

print(entropy(['male', 'male', 'male', 'male']))
print(entropy(['male', 'female', 'male', 'male']))
print(entropy(['female', 'male', 'female', 'male']))
print(entropy(['你好', '吗', '今天', '好多']))


