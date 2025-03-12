import pika, json

RABBITMQ_HOST = "localhost"
RABBITMQ_PORT = 5672
RABBITMQ_USER = "guest"  # Default username
RABBITMQ_PASS = "guest"  # Default password
QUEUE_NAME = "success_queue"

def get_rabbitmq_connection():
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
    return pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST, RABBITMQ_PORT, '/', credentials))

def get_rabbitmq_channel():
    connection = get_rabbitmq_connection()
    return connection.channel()

def publish_message(message):
    channel = get_rabbitmq_channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=json.dumps(message), properties=pika.BasicProperties(delivery_mode=2))
    print(f" [x] Sent {message}")
    connection = get_rabbitmq_connection()
    connection.close()

def consume_messages(callback):
    channel = get_rabbitmq_channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)
    print(f' [*] Worker started. Waiting for messages on queue "{QUEUE_NAME}".')
    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()