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
        username=config.get_env_var("RABBITMQ_USER"),
        password=config.get_env_var("RABBITMQ_PASSWORD")
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
    processor_class_name = config.get_env_var("PROCESSOR_TYPE")
    queue_name = config.get_env_var(
        processor_class_name+"_QUEUE_NAME")+config.get_env_var("QUEUE_NAME_PREFIX")
    channel.queue_declare(queue=queue_name, durable=True)

    message = {
        'event': 'TEST_EMAIL_EVENT',
        'data': dict(key1="value1", key2="value2"),
        'to_emails': ["janjua.afeef@gmail.com"]
    }
    # Publish a message to the queue
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=str.encode(json.dumps(message))
    )

    print("Message sent to RabbitMQ.")

    # Close the connection
    connection.close()
