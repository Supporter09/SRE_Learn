import pika

# Connect to RabbitMQ
credentials = pika.PlainCredentials('minh', 'minh')
parameters = pika.ConnectionParameters(
    host='localhost',
    virtual_host='/backend',
    credentials=credentials
)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Declare a queue (optional, but good practice)
channel.queue_declare(queue='test_queue', durable=True)

# Publish a message
channel.basic_publish(
    exchange='',
    routing_key='test_queue',
    body='Hello RabbitMQ!',
    properties=pika.BasicProperties(
        delivery_mode=2  # make message persistent
    )
)

print("✅ Message sent.")
connection.close()
