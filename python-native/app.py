from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/livenessprobe')
def live():
    return Response("{'status':'service is live'}", status=200, mimetype='application/json')

@app.route('/readinessprobe')
def ready():
    return Response("{'status':'service is ready'}", status=200, mimetype='application/json')