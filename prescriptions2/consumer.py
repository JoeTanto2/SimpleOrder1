from decouple import config
import pika, json
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prescriptions2.settings")
django.setup()
from entries.serializer import PrescriptionSerializer, PikUpSerializer
from entries.models import OurPrescriptions
params = pika.URLParameters(config('pika_params'))

connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='second')

def callback(ch, method, properties, body):
    info = json.loads(body)
    if properties.content_type == 'prescription_fill':
        serializer = PrescriptionSerializer(data=info)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
        else:
            print(serializer.errors)
    if properties.content_type == 'pickup':
        print('hi')
        print(f'info: {info}')
        object = OurPrescriptions.objects.filter(id=info).first()
        if object:
            serialized = PrescriptionSerializer(object)
            serializer = PikUpSerializer(data=serialized.data)
            if serializer.is_valid():
                serializer.save()
                object.delete()
                print('everything went through')
            else:
                print(serializer.errors)
channel.basic_consume(queue='second', on_message_callback=callback, auto_ack=True)

print('activated')
channel.start_consuming()


channel.close()