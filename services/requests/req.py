import requests
import time
import random

time.sleep(10)

for i in range(50):
    params = {'patient_id': i}
    data = {
        "age":random.randint(15,90),
        "sex":random.randint(0,1),
        "cp":random.randint(0,3),
        "trestbps":random.randint(70,220),
        "fbs":random.randint(0,1),
        "restecg":random.randint(0,2),
        "thalach":random.randint(60,220),
        "exang":random.randint(0,1),
        "oldpeak":random.uniform(0, 4.0),
        "slope":random.randint(0,2),
        "ca":random.randint(0,4),
        "thal":random.randint(1,3),
        } 
    response = requests.post('http://disease-predict:8000/api/prediction', params=params, json=data)
    time.sleep(random.randint(1,5))
    print(response.json())