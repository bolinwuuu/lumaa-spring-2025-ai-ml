FROM python:3.11-slim

ENV PYTHONWARNINGS="ignore"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY recommend.py .
COPY data/movie_500.csv data/movie_500.csv

ENTRYPOINT ["python", "recommend.py"]
