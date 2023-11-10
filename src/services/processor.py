"""
Base example of a service processor within the child image
"""

import logging
from rococo.messaging import BaseServiceProcessor

# Configure logging
logging.basicConfig(level=logging.INFO)


# This is an example implementation of a BaseServiceProcessor class.
class EmailServiceProcessor(BaseServiceProcessor):  # pylint: disable=R0903
    """
    Service processor that logs messages
    """

    def process(self, message):
        logging.info("Received message: %s to the service processor image!", message)

    def __init__(self):
        super().__init__()
