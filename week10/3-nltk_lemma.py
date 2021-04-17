#coding=utf8
"""
Created on Sun Nov 17 16:16:09 2019

@author: Neal LONG
"""
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import wordnet

def get_wordnet_pos(treebank_tag):
    """
    Translate the complext NLTK postag to simplied 
    wordnet definitions of postag
    """
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return 'n'

words = nltk.tokenize.word_tokenize('He was running and eating at same time. He ate a lot.')
word_tags = nltk.pos_tag(words)
wnl = WordNetLemmatizer()
print(wnl.lemmatize('going','n'))
print(wnl.lemmatize('going','v'))
print("="*20)
for word_tag in word_tags:   
    wornet_tag = get_wordnet_pos(word_tag[1])
    print(word_tag[0],"-->", 
          wnl.lemmatize(word_tag[0],wornet_tag))
