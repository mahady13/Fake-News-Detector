import streamlit as st
import nltk
import pickle
import string
import numpy as np
import pandas as pd
import sklearn
nltk.download('stopwords')
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
from nltk.tokenize import word_tokenize

import nltk
from nltk.corpus import stopwords
import string

stop_words = set(stopwords.words('english'))
punctuation = set(string.punctuation)


def preprocess_text(text):
    text = nltk.word_tokenize(text.lower())
    y = [ps.stem(i) for i in text if i.isalnum() and i not in stop_words]
    return " ".join(y)

tfidf=pickle.load(open('tfidf.pkl','rb'))
rfc=pickle.load(open('rfc.pkl','rb'))

st.title('Fake News Detector System')
inputtext=st.text_area('Enter the news here')

processed=preprocess_text(inputtext)
vectored=tfidf.transform([processed])
result=rfc.predict(vectored)[0]

if st.button('Predict'):
    if result == 0:
        st.header('This is Real News.')
    else:
        st.header('This is Fake News.')