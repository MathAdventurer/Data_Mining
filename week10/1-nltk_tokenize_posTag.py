#coding=utf8
"""
Created on Sun Nov 17 12:14:03 2019

@author: Neal LONG
"""

from nltk.tokenize import sent_tokenize, word_tokenize
import nltk

text = """All work and no play makes jack dull boy. 
        New York is great."""
 
#totenize sentences       
phrases = sent_tokenize(text)
print(phrases)
print("="*20)

#totenize words       
words = word_tokenize(text)
print(words)
print("="*20)

#pos tagging words
word_tags = nltk.pos_tag(words)
print(word_tags)
print("="*20)

#select specified words (proper noun here)
for word_tag in word_tags: 
    if word_tag[1] == 'NNP'  : 
        print(word_tag[0])
        
# import MWETokenizer() method from nltk 
from nltk.tokenize import MWETokenizer 


mwe = MWETokenizer() 

# Create a string input 
mwe.add_mwe(('All','work','and'))
mwe.add_mwe(('New','York'))


# tokenize witg mwe
mwe_words = mwe.tokenize(words) 
print(mwe_words) 


        

