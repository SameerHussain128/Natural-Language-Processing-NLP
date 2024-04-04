#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import nltk


# In[2]:


AI = '''As an AI language model, ChatGPT is designed to understand and generate human-like text responses in natural language.
 It has been trained on a vast amount of diverse internet text, allowing it to have a broad understanding of numerous topics. 
 However, it's important to note that ChatGPT's responses are generated based on patterns 
 and examples from its training data and may not always provide accurate or up-to-date information.'''


# In[3]:


AI


# In[4]:


type(AI)


# #### Tokenization

# In[5]:


sent = "my name is sam"


# In[6]:


sent


# In[7]:


from nltk.tokenize import word_tokenize


# In[8]:


sent_token = word_tokenize(sent)


# In[9]:


sent_token


# In[10]:


len(sent_token)


# In[11]:


AI_token = word_tokenize(AI)


# In[12]:


AI_token


# In[13]:


len(AI)


# In[14]:


len(AI_token)


# In[15]:


from nltk.probability import FreqDist

# number of times words repeated from the paragraph


# In[16]:


fdist = FreqDist()


# In[17]:


for word in AI_token:
   fdist[word.lower()]+=1
fdist


# In[18]:


fdist['text']


# In[19]:


fdist['chatgpt']


# In[20]:


fdist['language']


# In[21]:


len(fdist)

# Dubligates or repeated words are removed and length reduced


# ###
# * bigram - 2
# * trigram - 3
# * Ngram - more than 3
# words side by side
# 

# In[22]:


from nltk.util import bigrams, trigrams, ngrams


# In[23]:


string = '''As an AI language model, ChatGPT is designed to understand and generate human-like text responses in natural language.
 It has been trained on a vast amount of diverse internet text, allowing it to have a broad understanding of numerous topics. 
 However, it's important to note that ChatGPT's responses are generated based on patterns 
 and examples from its training data and may not always provide accurate or up-to-date information.'''


# In[24]:


bigram = list(nltk.bigrams(AI_token))


# In[25]:


bigram


# In[26]:


trigram = list(nltk.trigrams(AI_token))


# In[27]:


trigram


# In[28]:


ngram = list(nltk.ngrams(AI_token,4))


# In[29]:


ngram


# In[30]:


ngram = list(nltk.ngrams(AI_token,5))


# In[31]:


ngram


# In[32]:


ngram = list(nltk.ngrams(AI_token,10))


# In[33]:


ngram


# ###  Stemming
# 
# it will give root form or base form of the word

# In[34]:


from nltk.stem import PorterStemmer
pst = PorterStemmer()


# In[35]:


pst.stem('affectioned')


# In[36]:


words_to_stem = ['giving', 'give', 'loving', 'caring', 'typing', 'donating']
words_to_stem


# In[37]:


for words in words_to_stem:
    print(words+' : ' + pst.stem(words))


# In[38]:


from nltk.stem import LancasterStemmer
lst = LancasterStemmer()


# In[39]:


for words in words_to_stem:
    print(words+' : ' + lst.stem(words))


# ### Lematization
# 
# it will give complete meaningful information of the word

# In[40]:


from nltk.stem import wordnet
from nltk.stem import WordNetLemmatizer
word_lem = WordNetLemmatizer()


# In[41]:


words_to_stem


# In[42]:


for words in words_to_stem:
    print(words+ ' : ' + word_lem.lemmatize(words))


# # 
# porter stemmer    ---> (giving -- give) 
# 
# lancaster stemmer ---> (giving -- giv) 
# 
# wordnet lemmatizer --> (giving -- giving)
# 
# stemming vs lemmatizer :
# 
# stem - root or base form of the word || lemm - complete word

# ### Stopwords
# 
# In a sentence continuously speaking words || most repeated words 

# In[43]:


from nltk.corpus import stopwords


# In[44]:


stopwords.words('english')


# In[45]:


len(stopwords.words('english'))


# In[46]:


stopwords.words('arabic')


# In[47]:


len(stopwords.words('arabic'))


# In[48]:


stopwords.words('french')


# In[49]:


len(stopwords.words('french'))


# In[50]:


stopwords.words('chinese')


# In[51]:


len(stopwords.words('chinese'))


# In[52]:


stopwords.words('hindi')   # LOCAL LANGUAGE


# In[53]:


pip  install stopwords-hi
pip bower install stopwords-hi


# ### POS (part of speech)
# 
# it will give the grammar of the sentence

# In[54]:


sent = 'sam is natural when come to drawing'
sent


# In[55]:


sent_tokens =  word_tokenize(sent)
sent_tokens


# In[56]:


(len(sent_tokens))


# In[57]:


for token in sent_tokens:
    print(nltk.pos_tag([token]))


# # 
# Text Cleaning - Vectorization
# 
# text we will vectorize to number -- convert to 0 & 1
# 

# ## NLU - NATURAL LANGUAGE UNDERSTANDING
# 
# - Nltk - (tokens,stem,lemm,pos---)

# ## NLG - NATURAL LANGUAGE GENERATION

# ### Wordcloud

# In[58]:


from wordcloud import WordCloud
import matplotlib.pyplot as plt


# In[59]:


text = ('Python python python matplotlib sns sns matplotlib python machine learning machine learning deep learning deep learning AI deep learning nlp nlp nlp nlp nlp python sameer sameer spark spark pytorch AI AI')


# In[60]:


text


# In[61]:


wordcloud = WordCloud( width = 400, height = 200, margin = 0).generate(text)


# In[62]:


plt.imshow(wordcloud,interpolation = 'blackman')
plt.axis('off')
plt.margins(x=0,y=0)
plt.show()


# In[65]:


#stopwords = set(stopwords)
import numpy as np
mask = np.array(Image.open('heart.png'))

wordcloud = WordCloud( width = 480, height = 480, stopwords=stopwords,background_color = 'white', max_words=100,
                      contour_color='black',mask=mask, contour_width=3,colormap='rainbow').generate(text)

plt.figure()
plt.imshow(wordcloud,interpolation ='bilinear')
plt.axis("off")
plt.show()


# In[66]:


import matplotlib.pyplot as plt
from wordcloud import WordCloud

def generate_word_cloud(text, shape='rectangle'):
    wordcloud = WordCloud(background_color='white',
                          width=800,
                          height=400,
                          max_words=100,
                          relative_scaling=0.5,
                          colormap='Blues',
                          collocations=False,
                          shape=shape).generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


# In[67]:


wordcloud = WordCloud( width = 400, height = 200, margin = 0).generate(text)

import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np

def generate_word_cloud(text):
    # Load heart-shaped image
    heart_mask = np.array(Image.open("heart.png"))

    # Create word cloud with heart shape
    wordcloud = WordCloud(background_color='white',
                          width=800,
                          height=800,
                          max_words=100,
                          relative_scaling=0.5,
                          colormap='Blues',
                          collocations=False,
                          mask=heart_mask).generate(text)

    plt.figure(figsize=(8, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


# In[68]:


import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np

def generate_word_cloud(text):
    # Load heart-shaped image
    heart_mask = np.array(Image.open(r"D:\Data Science 6pm\wordcloud pics\heart.png"))

    # Create word cloud with heart shape
    wordcloud = WordCloud(background_color='white',
                          width=800,
                          height=800,
                          max_words=100,
                          relative_scaling=0.5,
                          colormap='Blues',
                          collocations=False,
                          mask=heart_mask).generate(text)

    plt.figure(figsize=(8, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# Example usage:
text = "Your text data goes here..."
generate_word_cloud(text)


# In[ ]:





# In[ ]:




