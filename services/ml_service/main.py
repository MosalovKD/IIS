from fastapi import FastAPI
from api_handler import FastAPIHandler

app = FastAPI()
app.handler = FastAPIHandler()

@app.get('/')
def root_dir():
    return({'Hello': 'world'})

@app.post('/api/prediction')
def make_prediction(patient_id: int, item_features: dict):
    prediction = app.handler.predict(item_features)
    return ({
             'disease': str(prediction),
             'patient_id': patient_id
            })