import os
import nltk
AI = '''Artificial Intelligence refers to the intelligence of machines. This is in contrast to the natural intelligence of 
humans and animals. With Artificial Intelligence, machines perform functions such as learning, planning, reasoning and 
problem-solving. Most noteworthy, Artificial Intelligence is the simulation of human intelligence by machines. 
It is probably the fastest-growing development in the World of technology and innovation. Furthermore, many experts believe
AI could solve major challenges and crisis situations.'''

AI
type(AI)

from nltk.tokenize import word_tokenize
AI_tokens = word_tokenize(AI)
AI_tokens
len(AI_tokens)

from nltk.tokenize import sent_tokenize
AI_sent = sent_tokenize(AI)
AI_sent
len(AI_sent)

AI

from nltk.tokenize import blankline_tokenize #Gives how many paragraphs
AI_blank = blankline_tokenize(AI)
AI_blank
len(AI_blank)

#NExt we will see how will use uni-gram, Bi-gram, Tri-gram using Nltk
from nltk.util import bigrams,trigrams,ngrams
string = 'the best and most beautifull thing in the world cannot be seen or even touched,they must be felt with heart'
quotes_tokens = word_tokenize(string)
# Print the tokens
print("Word Tokens:", quotes_tokens)
# Generate bigrams, trigrams, and ngrams
bigram_tokens = list(bigrams(quotes_tokens))
trigram_tokens = list(trigrams(quotes_tokens))
ngram_tokens = list(ngrams(quotes_tokens, 4))  # Example for 4-grams
# Print the n-grams
print("Bigrams:", bigram_tokens)
print("Trigrams:", trigram_tokens)
print("4-grams:", ngram_tokens)

len(quotes_tokens)


# Next we need to make some changes in tokens and that is called as stemming, stemming will gives you root form of a word
# also we will see some root form of the word & limitation of the word

#porter-stemmer
from nltk.stem import PorterStemmer
pst = PorterStemmer()
pst.stem('having')
pst.stem('running')
pst.stem('affection')
pst.stem('playing')
pst.stem('give')

words_to_stem  = ['give', 'given', 'giving', 'gave']
for words in  words_to_stem:
    print(words+ ':' + pst.stem(words))
    

words_to_stem=['give','giving','given','gave','thinking', 'loving', 'final', 'finalized', 'finally']
# i am giving these different words to stem, using porter stemmer we get the output
for words in words_to_stem:
    print(words+ ':' +pst.stem(words))
#in porterstemmer removes ing and replaces with e

#Lencasttemmer
#another stemmer known as lencastemmer stemmer and lets see what the different we will get hear
#stem the same thing using lencastemmer
from nltk.stem import LancasterStemmer
lst = LancasterStemmer()
for words in words_to_stem:
    print(words + ':' + lst.stem(words))
# lancasterstemmer is more aggresive then the porterstemmer


words_to_stem=['give','giving','given','gave','thinking', 'loving', 'final', 'finalized', 'finally']
# i am giving these different words to stem, using porter stemmer we get the output
for words in words_to_stem:
    print(words+ ':' +pst.stem(words))
    
    
#we have another stemmer called as snowball stemmer lets see about this snowball stemmer
from nltk.stem import SnowballStemmer
sbst = SnowballStemmer('english')
for words in words_to_stem:
    print(words+ ':' +sbst.stem(words))
#snowball stemmer is same as portstemmer
#different type of stemmer used based on different type of task
#if you want to see how many type of giv has occured then we will see the lancaster stemmer


#sometime stemming does not work & lets say e.g - fish,fishes & fishing all of them belongs to root word fish, 
#one hand stemming will cut the end & lemmatization will take into the morphological analysis of the word
from nltk.stem import wordnet
from nltk.stem import WordNetLemmatizer
word_lem = WordNetLemmatizer()
#Hear we are going to wordnet dictionary & we are going to import the wordnet lematizer

pst.stem('final')
lst.stem('finally')
sbst.stem('finalized')
lst.stem('final')
lst.stem('finalized')



# there is other concept called POS (part of speech) which deals with subject, noun, pronoun but before of this lets go with other concept called STOPWORDS
# STOPWORDS = i, is, as,at, on, about & nltk has their own list of stopewords 
from nltk.corpus import stopwords
stopwords.words('english') 
len(stopwords.words('english')) 

stopwords.words('spanish')
len(stopwords.words('spanish')) 

stopwords.words('french') 
len(stopwords.words('french')) 

stopwords.words('german') 
len(stopwords.words('german'))

stopwords.words('hindi') # research phase 
stopwords.words('marathi') 
stopwords.words('telugu') 


AI
AI_tokens
len(AI_tokens)


# we will see how to work in POS using NLTK library
sent = 'kathy is a natural when it comes to drawing'
sent_tokens = word_tokenize(sent)
sent_tokens
# first we will tokenize usning word_tokenize & then we will use pos_tag on all of the tokens 

for token in sent_tokens:
    print(nltk.pos_tag([token]))
    
    
sent2 = 'john is eating a delicious cake'
sent2_tokens = word_tokenize(sent2)
for token in sent2_tokens:
    print(nltk.pos_tag([token]))
    
    
# Another concept of POS is called NER ( NAMED ENTITIY RECOGNITION ), NER is the process of detecting name such as movie, moneytary value,organiztion, location, quantities & person
# there are 3 phases of NER - ( 1ST PHASE IS - NOUN PHRASE EXTRACTION OR NOUN PHASE IDENTIFICATION - This step deals with extract all the noun phrases from text using dependencies parsing and pos tagging
# 2nd step we have phrase classification - this is the classification where all the extracted nouns & phrase are classified into category such as location,names and much more 
# some times entity are misclassification 
# so if you are use NER in python then you need to import NER_CHUNK from nltk library

from nltk import ne_chunk
NE_sent = 'The US president stays in the WHITEHOUSE '

# IN NLTK also we have syntax- set of rules,principals & process 
# lets understand set of rules & that will indicates the syntax tree & in the real time also you have build this type of tree from the sentenses

# now lets understand the important concept called CHUNKING using the sentence structure
# chunking means grouping of words into chunks & lets understand the example of chunking 
# chunking will help to easy process the data
NE_tokens = word_tokenize(NE_sent)
#after tokenize need to add the pos tags
NE_tokens

NE_tags = nltk.pos_tag(NE_tokens)
NE_tags

#we are passin the NE_NER into ne_chunks function and lets see the outputs
NE_NER = ne_chunk(NE_tags)
print(NE_NER)

new = 'the big cat ate the little mouse who was after fresh cheese'
new_tokens = nltk.pos_tag(word_tokenize(new))
new_tokens
# tokenize done and lets add the pos tags also

# Libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Create a list of word
text=("Python Python Python Matplotlib Matplotlib Seaborn Network Plot Violin Chart Pandas Datascience Wordcloud Spider Radar Parrallel Alpha Color Brewer Density Scatter Barplot Barplot Boxplot Violinplot Treemap Stacked Area Chart Chart Visualization Dataviz Donut Pie Time-Series Wordcloud Wordcloud Sankey Bubble")
text

# Create the wordcloud object
wordcloud = WordCloud(width=480, height=480, margin=0).generate(text) 
# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()


