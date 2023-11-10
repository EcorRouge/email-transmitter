from . import EmailService
from ..config import SESConfig


class SESService(EmailService):

    def __init__(self):
        pass

    def __call__(self, settings: SESConfig, *args, **kwargs):
        super().__call__(settings)

    def send_message(self, event_name: str, event_data: dict, to_addresses: list):
        pass
