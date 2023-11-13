"""
Base example of a service processor within the child image
"""
import logging

from rococo.config import BaseConfig
from rococo.messaging import BaseServiceProcessor

from .factory import email_factory

logging.basicConfig(level=logging.INFO)


class EmailServiceProcessor(BaseServiceProcessor):
    """
    Service processor that sends emails
    """
    email_service = None

    def __init__(self):
        super().__init__()

        config = BaseConfig().get_env_vars()
        self.email_service = email_factory.get(**config)

        assert self.email_service is not None

    def process(self, message):
        logging.info("Received message: %s to the service processor image!", message)
        response = self.email_service.send_email(message)
