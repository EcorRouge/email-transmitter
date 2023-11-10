import re

from mailjet_rest import Client
from logger import logger

from . import EmailService
from ..config import MailjetConfig


class MailjetService(EmailService):

    def __init__(self):
        pass

    def __call__(self, settings: MailjetConfig, *args, **kwargs):
        super().__call__(settings)

        match = re.match('^(.*)\s*<(.*)>$', self.settings.SOURCE_EMAIL)
        name, email = match.groups()
        self.from_address = {"Name": name, "Email": email}

        self.client = Client(
            auth=(self.settings.MAILJET_API_KEY, self.settings.MAILJET_API_SECRET),
            version=self.settings.MAILJET_API_VERSION
        )

    def send_message(self, event_name: str, event_data: dict, to_addresses: list):
        event_mapping = self.settings.get_event(event_name)
        data = {
            'Messages': [
                {
                    "From": self.from_address,
                    "To": [{'Email': email} for email in to_addresses],
                    "TemplateLanguage": True,
                    "TemplateID": event_mapping['id'][self.settings.SERVICE_NAME],
                    "Variables": event_data
                }
            ]
        }
        if self.settings.ERROR_REPORTING_EMAIL:
            data['Messages'][0]['TemplateErrorReporting'] = {
                'Email': self.settings.ERROR_REPORTING_EMAIL
            }

        result = self.client.send.create(data=data)
        logger.debug('Source: {}'.format(data['Messages'][0]['From']))
        logger.debug('Destination: {}'.format(data['Messages'][0]['To']))
        logger.debug('Template: {}'.format(data['Messages'][0]['TemplateID']))
        logger.debug('TemplateData: {}'.format(data['Messages'][0]['Variables']))

        logger.debug('Status Code: {}'.format(result.status_code))
        logger.debug('Response: {}'.format(result.text))
