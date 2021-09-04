from decouple import config
import pika

params = pika.URLParameters(config('pika_params'))

connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='prescriptions')

def callback(ch, method, properties, body):
    print('received message')
    print(body)




channel.basic_consume(queue='prescriptions', on_message_callback=callback, auto_ack=True)

print('started consuming')

channel.start_consuming()


channel.close()