"""
Base example of a service processor within the child image
"""
import logging

from rococo.config import BaseConfig
from rococo.messaging import BaseServiceProcessor

from rococo.emailing.factory import email_factory

# Create a custom logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create a formatter
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(module)s:%(lineno)d - %(message)s')

# Create a handler and set the formatter
handler = logging.StreamHandler()
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

class EmailServiceProcessor(BaseServiceProcessor):
    """
    Service processor that sends emails
    """
    email_service = None

    def __init__(self):
        super().__init__()

        config = BaseConfig()
        if config.get_env_var("EMAIL_PROVIDER").lower() == "mailjet":
            logger.info("MailJet API Key : %s",config.get_env_var("MAILJET_API_KEY"))
            if config.get_env_var("MAILJET_API_KEY") in [None, "", False]:
                raise ValueError("MAILJET_API_KEY cant be empty")
            if config.get_env_var("MAILJET_API_SECRET") in [None,"",False]:
                raise ValueError("MAILJET_API_SECRET cant be empty")
        self.email_service = email_factory.get(**config.get_env_vars())

        assert self.email_service is not None

    def process(self, message):
        logger.info("Received message: %s to the service processor image!", message)
        response = self.email_service.send_email(message)
