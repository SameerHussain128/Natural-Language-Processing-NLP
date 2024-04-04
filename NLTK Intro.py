#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import nltk
#nltk.download()


# In[2]:


# you can also create your own words 

AI = '''Artificial Intelligence refers to the intelligence of machines. This is in contrast to the natural intelligence of 
humans and animals. With Artificial Intelligence, machines perform functions such as learning, planning, reasoning and 
problem-solving. Most noteworthy, Artificial Intelligence is the simulation of human intelligence by machines. 
It is probably the fastest-growing development in the World of technology and innovation. Furthermore, many experts believe
AI could solve major challenges and crisis situations.'''


# In[3]:


AI


# In[4]:


type(AI)


# In[5]:


from nltk.tokenize import word_tokenize


# In[6]:


AI_tokens = word_tokenize(AI)
AI_tokens


# In[7]:


len(AI)


# In[8]:


len(AI_tokens)


# In[9]:


from nltk.tokenize import sent_tokenize 


# In[10]:


AI_sent = sent_tokenize(AI)
AI_sent


# In[11]:


len(AI_sent)


# In[12]:


AI


# In[13]:


from nltk.tokenize import blankline_tokenize # GiVE YOU HOW MANY PARAGRAPH
AI_blank = blankline_tokenize(AI) 
AI_blank
#AI_blank


# In[14]:


len(AI_blank) 


# In[15]:


# NEXT WE WILL SEE HOW WE WILL USE UNI-GRAM,BI-GRAM,TRI-GRAM USING NLTK

from nltk.util import bigrams,trigrams,ngrams 


# In[16]:


string = 'the best and most beautifull thing in the world cannot be seen or even touched,they must be felt with heart'
quotes_tokens = nltk.word_tokenize(string)


# In[17]:


quotes_tokens


# In[18]:


len(quotes_tokens)


# In[19]:


quotes_bigrams = list(nltk.bigrams(quotes_tokens))
quotes_bigrams


# In[20]:


quotes_tokens


# In[21]:


quotes_trigrams = list(nltk.trigrams(quotes_tokens))
quotes_trigrams


# In[22]:


quotes_trigrams = list(nltk.ngrams(quotes_tokens, 3))
quotes_trigrams


# In[23]:


quotes_ngrams = list(nltk.ngrams(quotes_tokens, 4)) 
quotes_ngrams

#it has given n-gram of length 4


# In[24]:


len(quotes_tokens)


# In[25]:


quotes_ngrams_1 = list(nltk.ngrams(quotes_tokens, 5)) 
quotes_ngrams_1


# In[26]:


quotes_ngrams = list(nltk.ngrams(quotes_tokens, 9)) 
quotes_ngrams


# In[27]:


quotes_ngrams = list(nltk.ngrams(quotes_tokens, 24)) 
quotes_ngrams


# In[28]:


quotes_ngrams = list(nltk.ngrams(quotes_tokens, 23)) 
quotes_ngrams


# ## PorterStemmer

# In[29]:


# Next we need to make some changes in tokens and that is called as stemming, stemming will gives you root form of an word
# also we will see some root form of the word & limitation of the word

#porter-stemmer
from nltk.stem import PorterStemmer
pst = PorterStemmer()


# In[30]:


pst.stem('having') #stem will gives you the root form of the word 


# In[31]:


pst.stem('affection')


# In[32]:


pst.stem('playing')


# In[33]:


pst.stem('give')


# In[34]:


words_to_stem=['give','giving','given','gave']
for words in words_to_stem:
    print(words+  ':' + pst.stem(words))


# In[35]:


words_to_stem=['give','giving','given','gave','thinking', 'loving', 'final', 'finalized', 'finally']
# i am giving these different words to stem, using porter stemmer we get the output

for words in words_to_stem:
    print(words+ ':' +pst.stem(words))
    
#in porterstemmer removes ing and replaces with e


# ## LancasterStemmer

# In[36]:


#another stemmer known as lencastemmer stemmer and lets see what the different we will get hear
#stem the same thing using lencastemmer

from nltk.stem import LancasterStemmer
lst = LancasterStemmer()
for words in words_to_stem:
    print(words + ':' + lst.stem(words))
    
# lancasterstemmer is more aggresive then the porterstemmer


# In[37]:


words_to_stem=['give','giving','given','gave','thinking', 'loving', 'final', 'finalized', 'finally']
# i am giving these different words to stem, using porter stemmer we get the output

for words in words_to_stem:
    print(words+ ':' +pst.stem(words))


# ## SnowballStemmer 

# In[38]:


#we have another stemmer called as snowball stemmer lets see about this snowball stemmer

from nltk.stem import SnowballStemmer
sbst = SnowballStemmer('english')
for words in words_to_stem:
    print(words+ ':' +sbst.stem(words))
    
#snowball stemmer is same as portstemmer
#different type of stemmer used based on different type of task
#if you want to see how many type of giv has occured then we will see the lancaster stemmer


# In[39]:


#sometime stemming does not work & lets say e.g - fish,fishes & fishing all of them belongs to root word fish, 
#one hand stemming will cut the end & lemmatization will take into the morphological analysis of the word

from nltk.stem import wordnet
from nltk.stem import WordNetLemmatizer
word_lem = WordNetLemmatizer()

#Hear we are going to wordnet dictionary & we are going to import the wordnet lematizer


# In[40]:


words_to_stem


# In[41]:


#word_lem.lemmatize('corpora') #we get output as corpus 

#refers to a collection of texts. Such collections may be formed of a single language of texts, or can span multiple languages -- there are numerous reasons for which multilingual corpora (the plural of corpus) may be useful

for words in words_to_stem:
    print(words+ ':' +word_lem.lemmatize(words))


# In[42]:


pst.stem('final')


# In[43]:


lst.stem('finally')


# In[44]:


sbst.stem('finalized')


# In[45]:


lst.stem('final')


# In[46]:


lst.stem('finalized')


# In[47]:


# there is other concept called POS (part of speech) which deals with subject, noun, pronoun but before of this lets go with other concept called STOPWORDS
# STOPWORDS = i, is, as,at, on, about & nltk has their own list of stopewords 

from nltk.corpus import stopwords


# In[48]:


stopwords.words('english') 


# In[49]:


len(stopwords.words('english')) 


# In[50]:


stopwords.words('spanish')


# In[51]:


len(stopwords.words('spanish'))


# In[52]:


stopwords.words('french') 


# In[53]:


len(stopwords.words('french')) 


# In[54]:


stopwords.words('chinese') 


# In[55]:


len(stopwords.words('chinese')) 


# In[56]:


stopwords.words('german') 


# In[57]:


len(stopwords.words('german'))


# In[58]:


stopwords.words('arabic') 


# In[59]:


len(stopwords.words('arabic'))


# In[60]:


stopwords.words('urdu') 


# In[61]:


stopwords.words('hindi') # research phase 


# In[62]:


stopwords.words('telugu') 


# In[63]:


# first we need to compile from re module to create string that matched any digits or special character 
import re
punctuation = re.compile(r'[-.?!,:;()|0-9]') 

#now i am going to create to empty list and append the word without any punctuation & naming this as a post punctuation


# In[64]:


punctuation


# In[65]:


AI


# In[66]:


AI_tokens


# In[67]:


len(AI_tokens)


# ## Parts of Speech

# In[70]:


# we will see how to work in POS using NLTK library

sent = 'kabir is a natural when it comes to drawing'
sent_tokens = word_tokenize(sent)
sent_tokens

# first we will tokenize usning word_tokenize & then we will use pos_tag on all of the tokens


# In[71]:


for token in sent_tokens:
    print(nltk.pos_tag([token]))


# In[72]:


sent2 = 'john is eating a delicious cake'
sent2_tokens = word_tokenize(sent2)

for token in sent2_tokens:
    print(nltk.pos_tag([token]))


# In[82]:


# Another concept of POS is called NER ( NAMED ENTITIY RECOGNITION ), NER is the process of detecting name such as movie, moneytary value,organiztion, location, quantities & person
# there are 3 phases of NER - ( 1ST PHASE IS - NOUN PHRASE EXTRACTION OR NOUN PHASE IDENTIFICATION - This step deals with extract all the noun phrases from text using dependencies parsing and pos tagging
# 2nd step we have phrase classification - this is the classification where all the extracted nouns & phrase are classified into category such as location,names and much more 
# some times entity are misclassification 
# so if you are use NER in python then you need to import NER_CHUNK from nltk library


# In[83]:


from nltk import ne_chunk


# In[84]:


NE_sent = 'The US president stays in the WHITEHOUSE'


# In[76]:


# IN NLTK also we have syntax- set of rules,principals & process 
# lets understand set of rules & that will indicates the syntax tree & in the real time also you have build this type of tree from the sentenses

# now lets understand the important concept called CHUNKING using the sentence structure
# chunking means grouping of words into chunks & lets understand the example of chunking 
# chunking will help to easy process the data


# In[77]:


NE_tokens = word_tokenize(NE_sent)

#after tokenize need to add the pos tags
NE_tokens


# In[78]:


NE_tags = nltk.pos_tag(NE_tokens)
NE_tags


# In[79]:


#we are passin the NE_NER into ne_chunks function and lets see the outputs

NE_NER = ne_chunk(NE_tags)
print(NE_NER)


# In[80]:


new = 'the big cat ate the little mouse who was after fresh cheese'
new_tokens = nltk.pos_tag(word_tokenize(new))
new_tokens

# tokenize done and lets add the pos tags also


# ## Visualization through Wordcloud

# In[81]:


get_ipython().system('pip install Wordcloud')


# In[85]:


# Libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# In[86]:


# Create a list of word
text=("Python Python Python Matplotlib Matplotlib Seaborn Network Plot Violin Chart Pandas Datascience Wordcloud Spider Radar Parrallel Alpha Color Brewer Density Scatter Barplot Barplot Boxplot Violinplot Treemap Stacked Area Chart Chart Visualization Dataviz Donut Pie Time-Series Wordcloud Wordcloud Sankey Bubble")


# In[87]:


text


# In[88]:


# Create the wordcloud object
wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)


# In[89]:


# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()


# In[ ]:




