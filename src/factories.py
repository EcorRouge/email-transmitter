from typing import Type, Dict, Tuple

from services import EmailService, MailjetService, SESService, MailjetSettings, SESSettings, Settings


class EmailServiceFactory:
    def __init__(self):
        self._services: Dict[str, Tuple[EmailService, Type[Settings]]] = {}

    def register_service(self, key, service: EmailService, settings: Type[Settings]):
        self._services[key] = (service, settings)

    def _create(self, key, **kwargs):
        service_class, settings_class = self._services.get(key)

        if not service_class:
            raise ValueError(key)

        settings = settings_class(**kwargs)
        return service_class(settings=settings)

    def get(self, key, **kwargs):
        return self._create(key, **kwargs)


email_factory = EmailServiceFactory()
email_factory.register_service('mailjet', MailjetService(), MailjetSettings)
email_factory.register_service('ses', SESService(), SESSettings)
