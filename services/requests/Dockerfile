FROM python:3.11-slim

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python3", "req.py"]

# docker build . --tag request_service:0
# docker run request_service:0
