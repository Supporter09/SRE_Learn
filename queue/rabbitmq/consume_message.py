import pika

credentials = pika.PlainCredentials('minh', 'minh')
parameters = pika.ConnectionParameters(
    host='localhost',
    virtual_host='/backend',
    credentials=credentials
)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

def callback(ch, method, properties, body):
    print(f"📥 Received: {body.decode()}")

channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)

print('⏳ Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
