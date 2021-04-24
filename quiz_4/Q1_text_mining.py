#coding=utf8
"""
Created on Thu April 22 23:50:28 2021

@author: Neal LONG
"""

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
wiki_data = pd.read_csv('/Users/mac/Desktop/MDS5724_DataMining/Data_Mining_Codes/Data_Mining/quiz_4/wiki_people.csv', index_col = 'name')['text']
print(wiki_data.shape)
print(wiki_data.head())
name = 'Barack Obama'
text = wiki_data[name]

#==============
# Text feature extraction by CountVectorizer
count_vectorizer = CountVectorizer()
count_matrix = count_vectorizer.fit_transform([text])
features = count_vectorizer.get_feature_names()
data = pd.Series(count_matrix.toarray().flatten(), index = features).sort_values(ascending=False)
plt.figure(0) 
ax = data[:20].plot(kind='bar',figsize=(20,6),width=.8, fontsize=14,rot=55,title='Barack Obama Wikipedia Article Word Count')
plt.show()

#==============
# Text feature extraction by TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(wiki_data)
features = tfidf_vectorizer.get_feature_names()
row = wiki_data.index.get_loc(name)
data = pd.Series(tfidf_matrix.getrow(row).toarray().flatten(), index = features).sort_values(ascending=False)
plt.figure(1) 
ax = data[:20].plot(kind='bar', title='Barack Obama Wikipedia Article Word TF-IDF Values', figsize=(20,6), width = .8, fontsize=14,rot=55)
ax.title.set_size(20)
plt.show()

def compute_cosineSimilarity(text1,text2,tfidf_vec):
    return cosine_similarity(tfidf_vec.transform([text1]),tfidf_vec.transform([text2]))[0][0]
text1=wiki_data['Barack Obama']
text2=wiki_data['Hillary Rodham Clinton']
print(compute_cosineSimilarity(text1,text1,tfidf_vectorizer))
print(compute_cosineSimilarity(text1,text2,tfidf_vectorizer))

candidates= ['Barack Obama','Hillary Rodham Clinton','Joe Biden','Taylor Swift',u'Kelly Clarkson']

#==============
#Q1-2 insert your code here to recompute/show tfidf score of words being processed
# by TfidfVectorizer with extra paramters to remove English stop words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(wiki_data)
features = tfidf_vectorizer.get_feature_names()
row = wiki_data.index.get_loc(name)
data = pd.Series(tfidf_matrix.getrow(row).toarray().flatten(), index = features).sort_values(ascending=False)
plt.figure(1)
ax = data[:20].plot(kind='bar', title='Barack Obama Wikipedia Article Word TF-IDF Values', figsize=(20,6), width = .8, fontsize=14,rot=55)
ax.title.set_size(20)
plt.show()
print("The TOP THREE words:")
print(data[:3])
#==============
#Q1-3 insert your code here to compute pairwise cosine similarity among users
# listed in list "candidates" defined as above


def compute_cosineSimilarity(text1,text2,tfidf_vec):
    return cosine_similarity(tfidf_vec.transform([text1]),tfidf_vec.transform([text2]))[0][0]
record = dict()
candidates= ['Barack Obama','Hillary Rodham Clinton','Joe Biden','Taylor Swift',u'Kelly Clarkson']
for candidate in candidates:
    print(candidate+":")
    text1 = wiki_data[candidate]
    temp = candidates[:]
    temp.remove(candidate)
    record[candidate] = dict()
    for candidate_ in temp:
        text2 = wiki_data[candidate_]
        print(f'{candidate} with {candidate_}:','%.4f'%compute_cosineSimilarity(text1, text2, tfidf_vectorizer))
        record[candidate][compute_cosineSimilarity(text1, text2, tfidf_vectorizer)] = candidate_
    print("\n")
print("="*40)
print("The final result:")
for name in record.keys():
    print(name,record[name][max(record[name])],'%.4f'%max(record[name]))


