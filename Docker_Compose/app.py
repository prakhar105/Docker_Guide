import time

import redis
from flask import Flask

app=Flask(__name__)
cache=redis.Redis(host='redis',port=6379)

def get_hit_count():
    retries=5
    while True:
        try:
            #cache.reset_retry_count()
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -=1
            time.slep(0.5)

@app.route('/')

def hello():
    count=get_hit_count()
    return 'Hello Prakhar! I have been seen you {} times. \n'.format(count)

