FROM python:3.13-slim
WORKDIR /app
COPY requeriments.txt .
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     libgl1-mesa-glx \
#     libglib2.0-0 \
#     && rm -rf /var/lib/apt/lists/*
RUN pip install -r requeriments.txt