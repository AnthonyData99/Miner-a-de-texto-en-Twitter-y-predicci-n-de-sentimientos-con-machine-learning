import pandas as pd
import nltk
import re
import string
from textblob import TextBlob
import numpy as np
import csv
import time

from nltk .corpus import stopwords
from nltk import word_tokenize
nltk.download('stopwords')

df = pd.read_csv('df_fin.csv')

def transform(text):
  stopWords = set(stopwords.words('spanish'))
  text = str(text)
  text = re.sub(r'@[A-Za-z0-9]+', ' ', text) #Remover menciones @
  text = re.sub(r'RT[|\s]', ' ', text) # Remover RTs
  text = re.sub(r'#', ' ', text) #Remover # en el tweet
  text = re.sub(r'PedroCastillo', ' ', text) #Remover quesevayantodos
  #text = re.sub(r'QueseVayantodos', ' ', text)  #Quesevayantodos
  
  text = re.sub(r'https?:\/\/\S+', ' ', text) #Remover links

  pattern = r'''(?x)                    # set flag to allow verbose regexps
              (?:[A-Z]\.)+            # abbreviations, e.g. U.S.A
              | \w+(?:-\w+)*          # Words with optional internal hyphens
              | \$?\d+(?:\.\d+)?%?    # Currency and precentages, e.g. $12.40 82%
              | \.\.\.                # Ellipsis
              | [][.,;"'?():-_`]      #These are separate tokens; includes ],[
              '''
  words = nltk.regexp_tokenize(text, pattern)
  re_punc = re.compile('[%s]' % re.escape(string.punctuation)) # Remover signos de puntuacion
  stripped = [re_punc.sub('', w) for w in words]
  no_garbage = [w for w in stripped if  w.lower() not in stopWords] # Remover stopwords

  return (" ".join(no_garbage))

  #Quitar el steaming
  #reducir el dataset al máximo que permita correr
  
  
  df['tweets_transform'] = df['Tweet'].apply(transform)
  
  #Veremos qué palabras se repiten y no suman nada importante al estudio
  
 from wordcloud import WordCloud

text = df.tweets_transform
text = " ". join(df.tweets_transform)
wordcloud = WordCloud(width=1024, height=800, background_color='white', min_font_size=14).generate(text)
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
plt.figure(figsize = (8,8), facecolor = None)
plt.imshow(wordcloud)
plt.axis('off')
plt.tight_layout(pad = 0)
plt.show()

#guardamos el documento
df.to_csv("sentimientosDF-PedroCastill#.csv")

