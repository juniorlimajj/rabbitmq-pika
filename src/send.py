import pika, os, logging
logging.basicConfig()

url = os.environ.get('CLOUDAMQP_URL', 'amqp://rabbitmq:rabbitmq@localhost/%2f')
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='messageprocess')

channel.basic_publish(exchange='', routing_key='messageprocess', body='Test message')
print ("[->] Message sent to consumer")
connection.close()