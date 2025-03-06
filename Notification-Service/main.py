from notifications.email import sendEmailNotification
import sys, os
from client.rabbitMQClient import consume_messages

def callback(ch, method, properties, body):
    """RabbitMQ message callback function"""
    message_body = body.decode('utf-8')
    print(f" [>] Received message: {message_body[:100]}...")
    
    success = process_message(message_body)
    
    if success:
        print(" [✓] Processing completed successfully")
    else:
        print(" [✗] Failed to process message")
    
    # Acknowledge the message (remove from queue)
    ch.basic_ack(delivery_tag=method.delivery_tag)

def process_message(message):
    """Process the message and send email notification"""
    try:
        sendEmailNotification(message)
        return True
    except Exception as e:
        print(f" [✗] Failed to send email: {e}")
        return False

def main():
    """Start consuming messages from RabbitMQ"""
    consume_messages(callback)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)