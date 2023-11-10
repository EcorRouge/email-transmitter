from typing import Type, Dict, Tuple

from .base import EmailService
from .mailjet import MailjetService
from .ses import SESService
from .config import MailjetConfig, SESConfig, Config


class EmailServiceFactory:
    def __init__(self):
        self._services: Dict[str, Tuple[EmailService, Type[Config]]] = {}

    def register_service(self, key, service: EmailService, config: Type[Config]):
        self._services[key] = (service, config)

    def _create(self, key, **kwargs):
        service_class, config_class = self._services.get(key)

        if not service_class:
            raise ValueError(key)

        config = config_class(**kwargs)
        return service_class(config=config)

    def get(self, key, **kwargs):
        return self._create(key, **kwargs)


email_factory = EmailServiceFactory()
email_factory.register_service('mailjet', MailjetService(), MailjetConfig)
email_factory.register_service('ses', SESService(), SESConfig)
