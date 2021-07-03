from flask import Flask, Response
import pika

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

@app.route('/start_receive')
def receive():

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
    
    credentials = pika.PlainCredentials('python-native', 'python-native')
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq.sorting-queue.svc', 5672, '/', credentials))
    channel = connection.channel()
    # channel.queue_declare(queue='competition1')
    channel.basic_consume(queue='competition1', auto_ack=True, on_message_callback=callback)
    channel.start_consuming()
    return Response("{'status':'receive command accepted'}", status=201, mimetype='application/json')

