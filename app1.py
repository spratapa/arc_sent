import sys
import numpy as np 
import tensorflow as tf
from keras.models import Model,Sequential
from keras.layers import Dense, Input, Dropout, LSTM, Activation
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence,text
from matplotlib import pyplot
from keras.datasets import imdb
from keras.models import load_model

model = load_model('sentimentanalysis.h5')

        
# Import Flask for creating API
from flask import Flask, request
    
# Initialise a Flask object
app = Flask(__name__)

# Create an API endpoint for predicting
@app.route('/predict')

def predict_review():
   
    d = imdb.get_word_index()
    s1 = request.args.get('s1')    
    words = s1.split()
    review = []
    for word in words:
        if word not in d:
            review.append(2)
        else:
            review.append(d[word]+3)
    review = sequence.pad_sequences([review], maxlen = 2697)
    #print(review)
    prediction = model.predict(review)
    if prediction > 0.5:
        prediction = "Positive"
    else:
        prediction = "Negative"
   
# return the result back
    return  prediction

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)

