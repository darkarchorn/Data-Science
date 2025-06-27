# docker network create redis-network
# docker pull redis:latest
# docker run -d --name redis --network redis-network redis:latest

import os
import redis
from flask import Flask

app = Flask(__name__)
r = redis.Redis(host=os.environ.get("REDIS_HOST", "localhost"), port=6379)

@app.route('/')
def click():
    try:
        r.incr("clicks")
        return f"Clicks: {r.get('clicks').decode()}"
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
