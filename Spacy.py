#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("datascience and ai has great career ahead")


# In[3]:


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


text = """There are broadly two types of extractive summarization tasks depending on what the summarization program focuses on. The first is generic summarization, which focuses on obtaining a generic summary or abstract of the collection (whether documents, or sets of images, or videos, news stories etc.). The second is query relevant summarization, sometimes called query-based summarization, which summarizes objects specific to a query. Summarization systems are able to create both query relevant text summaries and generic machine-generated summaries depending on what the user needs.
An example of a summarization problem is document summarization, which attempts to automatically produce an abstract from a given document. Sometimes one might be interested in generating a summary from a single source document, while others can use multiple source documents (for example, a cluster of articles on the same topic). This problem is called multi-document summarization. A related application is summarizing news articles. Imagine a system, which automatically pulls together news articles on a given topic (from the web), and concisely represents the latest news as a summary.
Image collection summarization is another application example of automatic summarization. It consists in selecting a representative set of images from a larger set of images.[4] A summary in this context is useful to show the most representative images of results in an image collection exploration system. Video summarization is a related domain, where the system automatically creates a trailer of a long video. This also has applications in consumer or personal videos, where one might want to skip the boring or repetitive actions. Similarly, in surveillance videos, one would want to extract important and suspicious activity, while ignoring all the boring and redundant frames captured """


# In[8]:


import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation


# In[9]:


stopwords = list(STOP_WORDS) 
stopwords


# In[10]:


len(stopwords)


# In[11]:


nlp = spacy.load('en_core_web_sm') 


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


# In[20]:


#we have to calcualte the freaquency of each and every word, how many time word is repetation in text 

word_frequencies = {}

for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1


# In[21]:


word_frequencies
#print(word_frequencies)


# In[22]:


len(word_frequencies) 


# In[23]:


word_frequencies


# In[24]:


max_frequency = max(word_frequencies.values())
max_frequency 


# In[25]:


#to get normalized/weighted frequencies you should devide all frequencies with 11
for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_frequency


# In[26]:


#print(word_frequencies)
word_frequencies
#this is the normalized frequencies of each word


# In[32]:


sentence_tokens = [sent for sent in doc.sents]
sentence_tokens


# In[28]:


len(sentence_tokens)


# In[29]:


sentence_tokens = [sent for sent in doc.sents]
sentence_tokens


# In[34]:


# we are going to calculate the sentence score, to calculate the sentence score 
sentence_scores = {}

for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_frequencies[word.text.lower()]
            else:
                sentence_scores[sent] += word_frequencies[word.text.lower()]


# In[35]:


sentence_scores


# In[44]:


#lets say our case study was 30% sentence with maximum scores
from heapq import nlargest 


# In[48]:


select_length = int(len(sentence_tokens)*0.3)
select_length


# In[49]:


#we have to select maximum 4 sentences out of all sentences 
summary = nlargest(select_length,sentence_scores, key = sentence_scores.get)


# In[50]:


summary


# In[51]:


select_length = int(len(sentence_tokens)*0.4)
select_length


# In[52]:


#we have to select maximum 5 sentences out of all sentences 
summary = nlargest(select_length,sentence_scores, key = sentence_scores.get)


# In[53]:


summary


# In[54]:


sentence_scores


# In[55]:


print(summary)


# In[ ]:




