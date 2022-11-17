'''
command lines:

needed python 3.6

conda create -n chatbot python=3.6
activate chatbot
pip install nltk
pip install numpy
pip install tflearn
pip install tensorflow
'''

import json
import random
import tensorflow
import tflearn
import numpy
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()


with open("intents.json") as file:
    data = json.load(file)

words = []
labels = []
docs = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs.append(pattern)

        if intent["tag"] not in labels:
            labels.append(intent["tag"])
