#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install spacy')

get_ipython().system('python -m spacy download es_core_news_sm')


# In[2]:


import spacy
nlp = spacy.load("es_core_news_sm")


# In[3]:


doc = nlp("El gato está en la casa.")
for token in doc:
    print(token.text, token.pos_, token.dep_)


# In[4]:


text = """"La inteligencia artificial se fundó como disciplina académica en 1956 y, en los años transcurridos desde entonces, ha experimentado varias oleadas de optimismo,[5][6] seguidas de decepción y pérdida de financiación (conocido como "invierno de IA"),[7] [8] seguido de nuevos enfoques, éxito y financiación renovada.[6][9] La investigación de IA ha probado y descartado muchos enfoques diferentes desde su fundación, incluida la simulación del cerebro, el modelado de la resolución de problemas humanos, la lógica formal, las grandes bases de datos de conocimiento y la imitación del comportamiento animal. En las primeras décadas del siglo XXI, el aprendizaje automático altamente matemático-estadístico ha dominado el campo, y esta técnica ha demostrado ser muy exitosa, ayudando a resolver muchos problemas desafiantes en la industria y la academia.[9][10]

Los diversos subcampos de la investigación de IA se centran en objetivos particulares y el uso de herramientas particulares. Los objetivos tradicionales de la investigación de la IA incluyen el razonamiento, la representación del conocimiento, la planificación, el aprendizaje, el procesamiento del lenguaje natural, la percepción y la capacidad de mover y manipular objetos. -metas a plazo.[11] Para resolver estos problemas, los investigadores de IA han adaptado e integrado una amplia gama de técnicas de resolución de problemas, que incluyen búsqueda y optimización matemática, lógica formal, redes neuronales artificiales y métodos basados ​​en estadísticas, probabilidad y economía. AI también se basa en la informática, la psicología, la lingüística, la filosofía y muchos otros campos."""


# In[5]:


import spacy
from spacy.lang.es.stop_words import STOP_WORDS
from string import punctuation


# In[6]:


stopwords = list(STOP_WORDS) 
stopwords


# In[7]:


nlp = spacy.load('es_core_news_sm') 


# In[8]:


text


# In[9]:


doc = nlp(text)
doc


# In[10]:


# lets get the tokens from text
tokens = [token.text for token in doc]
print(tokens) 
#when we execute everythihg we created tokens from the text & not removed any of the stopwords & didnt cleaned the data


# In[11]:


punctuation # also called as noisy characters


# In[12]:


#we have to calcualte the freaquency of each and every word, how many time word is repetation in text 

word_frequencies = {}

for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1


# In[13]:


word_frequencies
#print(word_frequencies)


# In[14]:


max_frequency = max(word_frequencies.values())
max_frequency 


# In[15]:


#to get normalized/weighted frequencies you should devide all frequencies with 11
for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_frequency


# In[16]:


#print(word_frequencies)
word_frequencies
#this is the normalized frequencies of each word


# In[17]:


sentence_tokens = [sent for sent in doc.sents]
sentence_tokens


# In[18]:


len(sentence_tokens)


# In[19]:


# we are going to calculate the sentence score, to calculate the sentence score 
sentence_scores = {}

for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_frequencies[word.text.lower()]
            else:
                sentence_scores[sent] += word_frequencies[word.text.lower()]


# In[20]:


sentence_scores


# In[21]:


#lets say our case study was 30% sentence with maximum scores
from heapq import nlargest 


# In[22]:


select_length = int(len(sentence_tokens)*0.3)
select_length


# In[23]:


#we have to select maximum 4 sentences out of all sentences 
summary = nlargest(select_length,sentence_scores, key = sentence_scores.get)


# In[24]:


summary


# In[25]:


select_length = int(len(sentence_tokens)*0.4)
select_length


# In[26]:


#we have to select maximum 5 sentences out of all sentences 
summary = nlargest(select_length,sentence_scores, key = sentence_scores.get)


# In[27]:


summary


# In[28]:


sentence_scores


# In[29]:


print(summary)


# In[ ]:




