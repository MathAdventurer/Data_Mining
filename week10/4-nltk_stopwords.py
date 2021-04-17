#coding=utf8
"""
Created on Sun Nov 17 16:44:56 2019

@author: Neal LONG
"""

from nltk.corpus import stopwords
import nltk 

stop_words = set(stopwords.words('english'))
# remove following lines if you need punctuation 
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
words = nltk.tokenize.word_tokenize('He was running and eating at same time. He ate a lot.')
filtered_words = []
for word in words:
    low_word = word.lower()
    if low_word in stop_words:
        continue
    filtered_words.append(low_word)#normalize case
print(words)
print('='*20)
print(filtered_words)

