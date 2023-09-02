import numpy as np
import pickle
import pandas as pd
from flask import Flask, request

#model.pkl is used to getpredictions
app=Flask(__name__)
pickle_in=open("model (2).pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return"welcome All"
@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    input_cols=['MedInc','HouseAge','AveRooms','AveBedrms','Population','AveOccup','Latitude','Longitude']
    list1=[]
    for i in input_cols:
        val=request.args.get(i)
        list1.append(eval(val))
    prediction=classifier.predict([list1])
#prediction=classifier.predict([[varience,skewness]])
    print(prediction)
    return "Hello the answer is "+str(prediction)
if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)