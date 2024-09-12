import time
import redis
from flask import Flask
app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)
def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)
@app.route('/')
# A função hello() não diz olá.
def hello():
    count = get_hit_count()
    return 'Corinthians, o melhor time do mundo {} vezes e, quem concorda, respira.\n'.format(count)
