"""
Test module
"""
import json
import pika
from rococo.config import BaseConfig


def test_rabbitmq_send_message():
    """
    Establish a connection to RabbitMQ server
    """
    config = BaseConfig()

    credentials = pika.PlainCredentials(
        username=config.get_env_var("RABBITMQ_DEFAULT_USER"),
        password=config.get_env_var("RABBITMQ_DEFAULT_PASS")
    )
    parameters = pika.ConnectionParameters(
        host=config.get_env_var("RABBITMQ_HOST"),
        port=int(config.get_env_var("RABBITMQ_PORT")),
        virtual_host=config.get_env_var("RABBITMQ_VIRTUAL_HOST"),
        credentials=credentials
    )

    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue=config.get_env_var("RABBITMQ_QUEUE"), durable=True)

    # Publish a message to the queue
    channel.basic_publish(
        exchange='',
        routing_key=config.get_env_var("RABBITMQ_QUEUE"),
        body=json.dumps({"message": "Hello, RabbitMQ!"})
    )

    print("Message sent to RabbitMQ.")

    # Close the connection
    connection.close()
