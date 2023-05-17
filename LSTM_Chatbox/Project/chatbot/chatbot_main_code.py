# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 00:24:19 2020

@author: anshu
"""

#Loading intent Recognizer

from tensorflow.keras import models

    # write your code here

# loading tokenizer
import pickle

    # write your code here


#######################################################################
## Loading answers

import json
import numpy as np
answers = open("data/Ans_data.txt","r").read()
answers = answers.replace("'", "\"")
answers = json.loads(answers)
intents = list(answers.keys())

# Load configuration file

    # write your code here

#######################################################################
### chatbot flow


from tensorflow.keras.preprocessing.sequence import pad_sequences

while True:
    qus = input("You: ")
    if qus=='exit':
        print("Thank you for your time, Have a good day!")
        break
    
    # Make predictions
    
        # write your code here
    
    
    
    
    
    
