FROM python:3.13-alpine
WORKDIR /app
COPY requeriments.txt .
RUN pip install -r requeriments.txt