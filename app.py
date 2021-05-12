import uvicorn
from fastapi import FastAPI
from values import value
import numpy as np
import pickle
import pandas as pd
import json

app = FastAPI()
pickle_in = open("less_hydprice.pickle","rb")
model=pickle.load(pickle_in)
f = open('columns.json',)
data = json.load(f)
data_column = data['data_columns']

def predict_lass(property_size,bhk,Gymnasium,SwimmingPool,LiftAvailable,locality):    
    loc_index = data_column.index(locality.lower())

    x = np.zeros(len(data_column))
    x[0] = property_size
    x[1] = bhk
    x[2] = Gymnasium
    x[3] = SwimmingPool
    x[4] = LiftAvailable
    x[loc_index] = 1
    less = round(model.predict([x])[0])
    stringg = int(less/property_size)
    return less

@app.get('/')
def index():
    return {'message': 'Hyderabad House Price Prediction made by natwar koneru'}

@app.post('/predict')
def predict_price(data:value):
    data = data.dict()
    property_size= data['property_size']
    bhk= data['bhk']
    Gymnasium = data['Gymnasium']
    SwimmingPool= data['SwimmingPool']
    LiftAvailable= data['LiftAvailable']
    locality= data['locality']
    prediction = int(predict_lass(property_size,bhk,Gymnasium,SwimmingPool,LiftAvailable,locality))
    persqft = int(prediction/property_size)
    return {
        'prediction': prediction,
        'persqft' : persqft
    }
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

#uvicorn app:app --reload
