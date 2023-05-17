# -*- coding: utf-8 -*-

##########################################################################
# Data Preparation

import json
data = open("data/Qus_data.txt","r").read()
data = data.replace("'", "\"")
data = json.loads(data)

x = []
y = []
intents = list(data.keys())
for intent_name in intents:
    for sample in data[intent_name]:
        x.append(sample)
        y.append(intents.index(intent_name))

print(x,y)
##########################################################################
### Text Cleaning and Preprocessing
### intall the relevant packages
### pip install -U spacy
### python -m spacy download en_core_web_sm

import numpy as np
import spacy
nlp = spacy.load('en_core_web_sm')

# Remove stop words and perform lemmatization

    
    
    
    # write your code here




# Convert y into a numpy array


##########################################################################
### Training intent recognition model
        
# MAX_SEQUENCE_LENGTH = write your code here
MAX_WORDS = 500
EMBEDDING_DIM = 30

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


# Perform Tokenization


    #write your code here


# Perform padding to make sure that every document has same length


    #write your code here


#Onehot encode the labels
from tensorflow.keras.utils import to_categorical


    #write your code here


# Shuffle your training data
from sklearn.utils import shuffle


    #write your code here


# Training an LSTM Layer for intent recognition
from tensorflow.keras import models,layers

# Create a model






    #write your code here






# Compile your model


    #write your code here


# Train the model

    #write your code here

# Evaluate the model on xdata,y


    #write your code here

############################################################################
# Save the trained model

    #write your code here

#Saving the tokenizer
import pickle

    #write your code here

# create a Config dictionary which contains parameters last_accuracy, Max sequence length,
# Embedding dimension, Tokenizer name and model name

config = {}




    #write your code here




# write the dictionary into chatbot_config.txt file.


    #write your code here

