#coding=utf8
"""
Created on Sun Nov 17 12:29:00 2019

@author: Neal LONG
"""

import nltk

porter = nltk.stem.PorterStemmer()
lancaster = nltk.stem.LancasterStemmer()
snow = nltk.stem.SnowballStemmer('english')
word_list = ["playing", 'plays', 'played', "friendships", "friends","destabilize","is","ate","football"]
print("{0:20}{1:20}{2:20}{3:20}".format("Word","Porter Stemmer","lancaster Stemmer","Snow Stemmer"))
for word in word_list:
    print("{0:20}{1:20}{2:20}{3:20}".format(word,porter.stem(word),lancaster.stem(word),snow.stem(word)))
    
    
