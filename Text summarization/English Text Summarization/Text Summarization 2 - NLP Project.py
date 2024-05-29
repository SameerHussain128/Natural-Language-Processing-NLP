#!/usr/bin/env python
# coding: utf-8

# ### Text summarization of a paragraph
# * Choose random paragraph
# * Make into lower text 
# * Remove stop words and punctuation
# * Divide it into sentences and convert into summary
# * Hence large paragraph converted into short summary

# In[1]:


text = """In a world often dominated by negativity, it's important to remember the power of kindness and compassion. Small acts of kindness have the ability to brighten someone's day, uplift spirits, and create a ripple effect of positivity that can spread far and wide. Whether it's a smile to a stranger, a helping hand to a friend in need, or a thoughtful gesture to a colleague, every act of kindness has the potential to make a difference in someone's life. Beyond individual actions, there is also immense power in collective efforts to create positive change. When communities come together to support one another, incredible things can happen. From grassroots initiatives to global movements, people are uniting to tackle pressing social and environmental issues, driving meaningful progress and inspiring hope for a better future.It's also important to recognize the strength that lies within each and every one of us. We all have the ability to make a positive impact, no matter how small our actions may seem. By tapping into our innate compassion and empathy, we can cultivate a culture of kindness and empathy that enriches our lives and those around us.So let's embrace the power of kindness, and strive to make the world a better place one small act at a time. Together, we can create a brighter, more compassionate future for all."""


# In[2]:


# count length of text
len(text)


# In[3]:


import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation


# In[4]:


# check stopwords
stopwords = list(STOP_WORDS) 
stopwords


# In[5]:


# Length of stopwords
len(stopwords)


# In[6]:


nlp = spacy.load('en_core_web_sm') 


# In[7]:


doc = nlp(text)
doc


# In[8]:


# lets get the tokens from text
tokens = [token.text.lower() for token in doc
          if not token.is_punct and
          not token.is_punct and
          token.text !='\n']
print(tokens) 
# when we execute everythihg we created tokens from the text & not removed any of the stopwords & didnt cleaned the data


# In[9]:


tokens


# In[10]:


tokens1 = []
stopwords = list(STOP_WORDS)
allowed_pos = ['ADJ','PROPN','VERB','NOUN']
for token in doc:
    if token.text in stopwords or token.text in punctuation:
        continue
    if token.pos_ in allowed_pos:
        tokens1.append(token.text)


# In[11]:


tokens1


# In[12]:


print(tokens1)


# In[13]:


# Counter class is an tool for counting frequency of the elements in list
from collections import Counter
word_freq = Counter(tokens1)


# In[14]:


word_freq


# In[15]:


print(word_freq)


# In[16]:


max_freq = max(word_freq.values())


# In[17]:


max_freq


# In[18]:


#to get normalized/weighted frequencies you should devide all frequencies with 11
for word in word_freq.keys():                       # given word / max freq word  5/5 = 1
    word_freq[word] = word_freq[word]/max_freq          


# In[19]:


word_freq


# In[20]:


sent_token = [sent for sent in doc.sents]
sent_token


# In[21]:


print(sent_token)


# In[22]:


len(sent_token)


# In[23]:


# we are going to calculate the sentence score, to calculate the sentence score 
        
sent_score = {}
for sent in sent_token:
    for word in sent.text.split():
        word = word.lower()  # Convert word to lowercase to match the dictionary keys
        if word in word_freq.keys():
            if sent not in sent_score.keys():
                sent_score[sent] = word_freq[word]
            else:
                sent_score[sent] += word_freq[word]
        print(word)  # Print the word for debugging


# In[24]:


len(word)


# In[25]:


sent_score


# In[26]:


import pandas as pd
pd.DataFrame(list(sent_score.items()),columns=['Sentence','Score'])


# In[27]:


#lets say our case study was 30% sentence with maximum scores
from heapq import nlargest


# In[28]:


# Calculate the number of top sentences to select (30% of total sentences)
num_sentences = max(1, int(len(sent_token) * 0.3))


# In[29]:


num_sentences


# In[30]:


# Select the top sentences with the highest scores
top_sentences = nlargest(num_sentences, sent_score, key=sent_score.get)


# In[31]:


top_sentences


# In[32]:


# Create a DataFrame from the top sentences
df_top_sentences = pd.DataFrame([(sent.text, sent_score[sent]) for sent in top_sentences], columns=['Sentence', 'Score'])


# In[33]:


# Display the DataFrame and the summary
print(df_top_sentences)


# In[34]:


# Extract the text of the top sentences
top_sentences_text = [sent.text for sent in top_sentences]


# In[35]:


# Join the top sentences into a single string
summary = " ".join(top_sentences_text)


# In[36]:


print(summary)


# In[37]:


print("\nSummary of top sentences : ")
print()  # Print an empty line
print(summary)


# In[ ]:




