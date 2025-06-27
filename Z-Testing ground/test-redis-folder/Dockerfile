FROM python:3.10

WORKDIR /app
COPY test-redis.py .

RUN pip install flask redis

CMD ["python", "test-redis.py"]
