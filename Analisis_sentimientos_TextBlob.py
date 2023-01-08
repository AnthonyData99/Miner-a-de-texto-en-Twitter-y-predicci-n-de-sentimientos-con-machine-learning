
import pandas as pd
import nltk
import re
import string
from textblob import TextBlob
import numpy as np
import csv
import time

df = pd.read_csv('sentimientosDF-PedroCastill#.csv')
##estilo textblob
def get_polarity(text):
    analysis=TextBlob(text)
    if text != '':
        try:
                #if analysis.detect_language()=='es':
                result=analysis.translate(from_lang='es', to='en').sentiment.polarity
                time.sleep(5)
                return result

        except :
                pass
          
          
df['polarity'] = df['tweets_transform'].apply(get_polarity)
df
