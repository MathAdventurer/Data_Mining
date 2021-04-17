#coding=utf8
"""
Created on Sun Nov 17 17:26:53 2019

@author: Neal LONG
"""
from nltk.tokenize import  word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
import nltk

stop_words = set(stopwords.words('english'))
# remove following lines if you need punctuation 
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])

def get_wordnet_pos(treebank_tag):
    # transfer nltk pos tag to wordnet postag
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

def clean_tokenize_text(text,remove_stopwords=True):
    """
    Clean and tokenize text into words
    """
    #Step1:tokenize
    words = word_tokenize(text)
    #Step2:pos tagging
    word_tags = nltk.pos_tag(words)

    wnl = WordNetLemmatizer()
    filtered_words=[]
    
    for word_tag in word_tags:   
        wornet_tag = get_wordnet_pos(word_tag[1])
         #step3: Lemmatization or stemming
        word_lemma = wnl.lemmatize(word_tag[0],pos=wornet_tag)
        #step4: normalize case
        low_word_lemma = word_lemma.lower()
         #step5: remove stop words
        if remove_stopwords and low_word_lemma in stop_words: 
            continue
        filtered_words.append(low_word_lemma)
    # count word fequency
    return filtered_words

if __name__ == "__main__":
    clean_words = clean_tokenize_text('He was running and eating at same time. He ate a lot.')
    word_count = nltk.FreqDist(clean_words)
    word_count.tabulate()#print the word freq
    
    print("="*20)
    
    clean_words = clean_tokenize_text('I am not happy')
    word_count = nltk.FreqDist(clean_words)
    word_count.tabulate()
    
    print("="*20)
    
    clean_words = clean_tokenize_text('I am not happy',False)#without removing stopwords
    word_count = nltk.FreqDist(clean_words)
    word_count.tabulate()
    
    