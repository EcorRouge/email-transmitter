from abc import ABC, abstractmethod

from services.config.settings import EmailSettings


class EmailService(ABC):
    """
        Base class for email service providers
    """
    settings: EmailSettings

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __call__(self, settings: EmailSettings, *args, **kwargs):
        self.settings = settings

    @abstractmethod
    def send_message(self, event_name: str, event_data: dict, to_addresses: list):
        return NotImplementedError
