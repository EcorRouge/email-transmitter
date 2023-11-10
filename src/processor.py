"""
Base example of a service processor within the child image
"""

import logging

from rococo.config import BaseConfig
from rococo.messaging import BaseServiceProcessor

from emailing import EmailServiceProvider, email_factory

logging.basicConfig(level=logging.INFO)


class EmailServiceProcessor(BaseServiceProcessor):
    """
    Service processor that logs messages
    """
    email_service = None

    def __init__(self):
        super().__init__()

        self.email_service = email_factory.get(EmailServiceProvider.mailjet, **BaseConfig().get_env_vars())

    def process(self, message):
        logging.info("Received message: %s to the service processor image!", message)
        self.email_service.send_message(message)
