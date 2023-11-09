from typing import Type, Dict

from services import EmailService, MailjetService, SESService


class EmailServiceFactory:
    def __init__(self):
        self._services: Dict[str, EmailService] = {}

    def register_service(self, key, service: EmailService):
        self._services[key] = service

    def create(self, key, **kwargs):
        provider = self._services.get(key)

        if not provider:
            raise ValueError(key)

        return provider(**kwargs)

    def get(self, key, **kwargs):
        return self.create(key, **kwargs)


email_factory = EmailServiceFactory()
email_factory.register_service('mailjet', MailjetService())
email_factory.register_service('ses', SESService())
