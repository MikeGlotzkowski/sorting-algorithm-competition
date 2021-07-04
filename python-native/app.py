from flask import Flask, Response
from logging.config import dictConfig
from Consumer import ReconnectingMqttConsumer

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

@app.route('/startreceive')
def start_receive():
    amqp_url = "amqp://python-native:python-native@rabbitmq.sorting-queue.svc:5672/%2F"
    consumer = ReconnectingMqttConsumer(amqp_url, app.logger)
    consumer.run()


@app.route('/livenessprobe')
def live():
    app.logger.info('Livenessprobe was called.')
    return Response("{'status':'service is live'}", status=200, mimetype='application/json')


@app.route('/readinessprobe')
def ready():
    app.logger.info('Readinessprobe was called.')
    return Response("{'status':'service is ready'}", status=200, mimetype='application/json')

# def on_message(channel, method_frame, header_frame, body):
#     app.logger.info(method_frame.delivery_tag)
#     app.logger.info(method_frame.header_frame)
#     app.logger.info(body)
#     channel.basic_ack(delivery_tag=method_frame.delivery_tag)

# @app.route('/start_receive')
# def receive():
#     app.logger.info('start_receive was called.')
#     credentials = pika.PlainCredentials('python-native', 'python-native')
#     connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq.sorting-queue.svc', 5672, '/', credentials))
#     channel = connection.channel()
#     # channel.queue_declare(queue='competition1')
#     channel.basic_consume(queue='competition1', auto_ack=False, on_message_callback=on_message)
#     app.logger.info('Queue connection configured. Start consuming...')
#     channel.start_consuming()
