"""
Base example of a service processor within the child image
"""

import logging

from rococo.config import BaseConfig
from rococo.messaging import BaseServiceProcessor

from services.enums import EmailService
from services.factories import email_factory

logging.basicConfig(level=logging.INFO)
email_service = email_factory.get(EmailService.mailjet, **BaseConfig().get_env_vars())


class EmailServiceProcessor(BaseServiceProcessor):
    """
    Service processor that logs messages
    """

    def process(self, message):
        logging.info("Received message: %s to the service processor image!", message)
        email_service.send_email(message)

    def __init__(self):
        super().__init__()
