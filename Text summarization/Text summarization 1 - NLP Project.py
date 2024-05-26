#!/usr/bin/env python
# coding: utf-8

# ## Text summarization of a paragraph
# * Choose random paragraph
# * Make into lower text 
# * Remove stop words and punctuation
# * Divide it into sentences and convert into summary
# * Hence large paragraph converted into short summary

# In[1]:


# pip install spacy
# python -m spacy download en_core_web_sm (we have 3 type of model is available called small, medium, large)


# In[2]:


text = """There are broadly two types of extractive summarization tasks depending on what the summarization program focuses on. The first is generic summarization, which focuses on obtaining a generic summary or abstract of the collection (whether documents, or sets of images, or videos, news stories etc.). The second is query relevant summarization, sometimes called query-based summarization, which summarizes objects specific to a query. Summarization systems are able to create both query relevant text summaries and generic machine-generated summaries depending on what the user needs.
An example of a summarization problem is document summarization, which attempts to automatically produce an abstract from a given document. Sometimes one might be interested in generating a summary from a single source document, while others can use multiple source documents (for example, a cluster of articles on the same topic). This problem is called multi-document summarization. A related application is summarizing news articles. Imagine a system, which automatically pulls together news articles on a given topic (from the web), and concisely represents the latest news as a summary.
Image collection summarization is another application example of automatic summarization. It consists in selecting a representative set of images from a larger set of images.[4] A summary in this context is useful to show the most representative images of results in an image collection exploration system. Video summarization is a related domain, where the system automatically creates a trailer of a long video. This also has applications in consumer or personal videos, where one might want to skip the boring or repetitive actions. Similarly, in surveillance videos, one would want to extract important and suspicious activity, while ignoring all the boring and redundant frames captured """


# In[3]:


import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation


# In[4]:


stopwords = list(STOP_WORDS) 
stopwords


# In[5]:


len(stopwords)


# In[6]:


nlp = spacy.load('en_core_web_sm') 


# In[7]:


text


# In[8]:


doc = nlp(text)
doc


# In[9]:


# lets get the tokens from text
tokens = [token.text for token in doc]
print(tokens) 
#when we execute everythihg we created tokens from the text & not removed any of the stopwords & didnt cleaned the data


# In[10]:


tokens


# In[11]:


len(tokens)


# In[12]:


punctuation # also called as noisy characters


# In[13]:


doc


# In[14]:


#we have to calcualte the freaquency of each and every word, how many time word is repetation in text 

word_frequencies = {}

for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1


# In[15]:


word_frequencies
#print(word_frequencies)


# In[16]:


len(word_frequencies) 


# In[17]:


word_frequencies


# In[18]:


max_frequency = max(word_frequencies.values())
max_frequency 


# In[19]:


#to get normalized/weighted frequencies you should devide all frequencies with 11
for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_frequency


# In[20]:


#print(word_frequencies)                                   current word/max repeated word -- 1/11
word_frequencies
#this is the normalized frequencies of each word


# In[21]:


sentence_tokens = [sent for sent in doc.sents]
sentence_tokens


# In[22]:


len(sentence_tokens)


# In[23]:


sentence_tokens = [sent for sent in doc.sents]
sentence_tokens


# In[24]:


# we are going to calculate the sentence score, to calculate the sentence score 
sentence_scores = {}

for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_frequencies[word.text.lower()]
            else:
                sentence_scores[sent] += word_frequencies[word.text.lower()]


# In[25]:


sentence_scores


# In[26]:


#lets say our case study was 30% sentence with maximum scores
from heapq import nlargest 


# In[27]:


select_length = int(len(sentence_tokens)*0.3)
select_length


# In[28]:


#we have to select maximum 4 sentences out of all sentences 
summary = nlargest(select_length,sentence_scores, key = sentence_scores.get)


# In[29]:


summary


# In[30]:


select_length = int(len(sentence_tokens)*0.4)
select_length


# In[31]:


#we have to select maximum 5 sentences out of all sentences 
summary = nlargest(select_length,sentence_scores, key = sentence_scores.get)


# In[32]:


summary


# In[33]:


sentence_scores


# In[34]:


print(summary)

