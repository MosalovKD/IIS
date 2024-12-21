from fastapi import FastAPI, HTTPException
from api_handler import FastAPIHandler
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Histogram, Gauge, Counter, Summary

app = FastAPI()
app.handler = FastAPIHandler()

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

prediction_metric = Histogram(
    'prediction_metric_histogram',
    'Histogram of model predictions (0 or 1)',
    buckets=(0.1, 1.1)
)

request_counter = Counter('request_counter', 'Number of requests received')

@app.get('/')
def root_dir():
    return({'Hello': 'world'})

@app.post('/api/prediction')
def make_prediction(patient_id: int, item_features: dict):

    prediction = app.handler.predict(item_features)

    request_counter.inc()
    prediction_metric.observe(prediction)

    return ({
            'disease': str(prediction),
            'patient_id': patient_id
            })
