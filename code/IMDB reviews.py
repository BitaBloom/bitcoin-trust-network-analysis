#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import string
import nltk
import os


# In[2]:


dataset = pd.read_csv("IMDB Dataset.csv")


# In[3]:


dataset


# In[4]:


from nltk.corpus import stopwords
stopwords.words('english')


# In[5]:


dataset


# In[6]:


dataset.drop(dataset.columns[[1]], axis = 1)


# In[7]:


# Load the regular expression library
import re


# In[8]:


dir(string)


# In[9]:


#punctuations
string.punctuation


# In[10]:


dataset['review_processed'] = dataset['review'].map(lambda x: re.sub('[,\.!?]', '', x))


# In[11]:


dataset['review_processed'].head()


# In[12]:


from wordcloud import WordCloud
# Join the different processed titles together.
long_string = ','.join(list(dataset['review_processed'].values))
# Create a WordCloud object
wordcloud = WordCloud(background_color="white", max_words=1000, contour_width=3, contour_color='steelblue')
# Generate a word cloud
wordcloud.generate(long_string)

# Visualize the word cloud
wordcloud.to_image()


# In[13]:


import gensim
from gensim.utils import simple_preprocess
import nltk
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
stop_words.extend(['from', 'subject', 're', 'edu', 'use'])
def sent_to_words(sentences):
    for sentence in sentences:
        # deacc=True removes punctuations
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))

def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) 
             if word not in stop_words] for doc in texts]


# In[14]:


data = dataset.review_processed.values.tolist()
data_words = list(sent_to_words(data))
# remove stop words
data_words = remove_stopwords(data_words)

print(data_words[:1][0][:30])


# In[15]:


import gensim.corpora as corpora

# Create Dictionary
id2word = corpora.Dictionary(data_words)

# Create Corpus
texts = data_words

# Term Document Frequency
corpus = [id2word.doc2bow(text) for text in texts]

# View
print(corpus[:1][0][:30])


# In[16]:


from pprint import pprint

# number of topics
num_topics = 10

# Build LDA model
lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                       id2word=id2word,
                                       num_topics=num_topics)

# Print the Keyword in the 10 topics
pprint(lda_model.print_topics())
doc_lda = lda_model[corpus]


# In[17]:


lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=7,
                                           random_state=100,
                                           update_every=1,
                                           chunksize=100,
                                           passes=10,
                                           alpha="auto")


# In[18]:


pyLDAvis.enable_notebook()
vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, id2word, mds="mmds", R=30)
vis


# In[19]:


pyLDAvis.enable_notebook()
vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, id2word, mds="mmds", R=30)
vis


# In[20]:



import pyLDAvis.gensim_models

import pickle 
import pyLDAvis


# In[21]:


lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=7,
                                           random_state=100,
                                           update_every=1,
                                           chunksize=100,
                                           passes=10,
                                           alpha="auto")


# In[22]:


pyLDAvis.enable_notebook()
vis = pyLDAvis.gensim_models.prepare(lda_model, corpus, id2word, mds="mmds", R=30)
vis


# In[ ]:




