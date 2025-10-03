FROM python:3.13

WORKDIR /app
COPY requeriments.txt .
RUN pip install -r requeriments.txt