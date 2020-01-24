import pika, os, time

def message_process_function(msg):
  print(" message processing")
  print(" [->] Received " + str(msg))
  time.sleep(5)
  print(" message processing finished")

url = os.environ.get('CLOUDAMQP_URL', 'amqp://rabbitmq:rabbitmq@localhost:5672/%2f')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='messageprocess')

def callback(ch, method, properties, body):
  message_process_function(body)

channel.basic_consume('messageprocess',
  callback,
  auto_ack=True)

channel.start_consuming()
connection.close()