from flask import Flask
import random
from flask import Response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'

@app.route('/ready')
def ready():
    # ready on evan numbers
    r = random.randint(0,9)
    if r % 2 == 0:
        return Response("{'status':'ready'}", status=200, mimetype='application/json')
    return Response("{'status':'not ready'}", status=503, mimetype='application/json')


@app.route('/healthy')
def healthy():
    r = random.randint(0,9)
    if r % 5 == 0:
        return Response("{'status':'healthy'}", status=200, mimetype='application/json')
    return Response("{'status':'not healthy'}", status=503, mimetype='application/json')