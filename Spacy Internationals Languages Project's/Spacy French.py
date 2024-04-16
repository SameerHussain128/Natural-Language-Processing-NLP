#!/usr/bin/env python
# coding: utf-8

# In[1]:


# !python -m spacy download fr_core_news_sm


# In[2]:


import spacy
# from spacy.lang.fr.examples import sentences 


# In[3]:


nlp = spacy.load("fr_core_news_sm")
doc = nlp("salut comment vas-tu? je vais bien.")
for token in doc:
    print(token.text)


# In[4]:


for token in doc:
    print(token.pos)


# In[5]:


for token in doc:
    print(token.pos_)


# In[6]:


for token in doc:
    print(token.text, token.pos_)


# In[7]:


doc = nlp("salut comment vas-tu? je vais bien.")
for token in doc:
    print(token.text, token.pos_, token.dep_)


# In[8]:


text = """La ville de Paris est connue dans le monde entier pour sa beauté et son histoire fascinante. Chaque coin de rue raconte une histoire différente, des boulevards animés aux ruelles pittoresques. Les cafés parisiens sont des lieux emblématiques où l'on peut savourer un café délicieux tout en observant le monde passer. La Tour Eiffel, symbole de la ville, se dresse majestueusement au-dessus de l'horizon, offrant une vue imprenable sur la capitale française. Paris est véritablement une ville où l'art, la culture et la gastronomie se rencontrent pour créer une expérience inoubliable pour tous ceux qui la visitent."""


# In[9]:


#import spacy
from spacy.lang.fr.stop_words import STOP_WORDS
from string import punctuation


# In[10]:


stopwords = list(STOP_WORDS) 
stopwords


# In[11]:


len(stopwords)


# In[12]:


text


# In[13]:


doc = nlp(text)
doc


# In[14]:


# lets get the tokens from text
tokens = [token.text for token in doc]
print(tokens) 
#when we execute everythihg we created tokens from the text & not removed any of the stopwords & didnt cleaned the data


# In[15]:


tokens


# In[16]:


len(tokens)


# In[17]:


punctuation # also called as noisy characters


# In[18]:


doc


# In[19]:


#we have to calcualte the freaquency of each and every word, how many time word is repetation in text 

word_frequencies = {}

for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1


# In[20]:


word_frequencies
#print(word_frequencies)


# In[21]:


len(word_frequencies) 


# In[22]:


max_frequency = max(word_frequencies.values())
max_frequency 


# In[23]:


#to get normalized/weighted frequencies you should devide all frequencies with 11
for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_frequency


# In[24]:


#print(word_frequencies)
word_frequencies
#this is the normalized frequencies of each word


# In[25]:


sentence_tokens = [sent for sent in doc.sents]
sentence_tokens


# In[26]:


sentence_tokens = [sent for sent in doc.sents]
sentence_tokens


# In[27]:


# we are going to calculate the sentence score, to calculate the sentence score 
sentence_scores = {}

for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_frequencies[word.text.lower()]
            else:
                sentence_scores[sent] += word_frequencies[word.text.lower()]


# In[28]:


sentence_scores


# In[29]:


#lets say our case study was 30% sentence with maximum scores
from heapq import nlargest 


# In[30]:


select_length = int(len(sentence_tokens)*0.3)
select_length


# In[31]:


#we have to select maximum 4 sentences out of all sentences 
summary = nlargest(select_length,sentence_scores, key = sentence_scores.get)


# In[32]:


summary


# In[33]:


select_length = int(len(sentence_tokens)*0.4)
select_length


# In[34]:


#we have to select maximum 5 sentences out of all sentences 
summary = nlargest(select_length,sentence_scores, key = sentence_scores.get)
summary


# In[35]:


sentence_scores


# In[36]:


print(summary)

