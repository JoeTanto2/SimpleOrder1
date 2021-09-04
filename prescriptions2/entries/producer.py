from decouple import config
import pika, json

params = pika.URLParameters(config('pika_params'))

connection = pika.BlockingConnection(params)
channel = connection.channel()

if not connection or connection.is_closed:
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

def publish (method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='second', body=json.dumps(body), properties=properties)