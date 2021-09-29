import time
import redis 
from flask import Flask
from flask_restful import Api

from .api import api as backend

app = Flask(__name__)
api = Api(app)

app =  Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retires = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retires == 0:
                raise exc
            retires -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f'Hello World, from Docker! I have been Seen {count} times. \n'

@app.route('/api', methods=['GET'])
def backend_get():
    count = get_hit_count()
    data = backend.get(app)
    return f'Hello World, from Docker! I have been Seen {count} times. \n'


@app.route('/api', methods=['POST'])
def backend_post():
    count = get_hit_count()
    data = backend.post(app)
    return f'Hello World, from Docker! I have been Seen {count} times. \n'

