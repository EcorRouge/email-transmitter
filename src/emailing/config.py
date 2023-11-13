import json
import os.path
from typing import Dict

from pydantic import BaseSettings, Extra

from .enums import EmailProvider


class Config(BaseSettings):
    CONFIG_FILEPATH: str
    EMAIL_PROVIDER: EmailProvider

    _config: Dict = {}

    class Config:
        extra = Extra.ignore

    def read_config(self):
        if not os.path.isfile(self.CONFIG_FILEPATH):
            raise OSError(f'Config.json file not found on specified path. {self.CONFIG_FILEPATH}')

        with open(self.CONFIG_FILEPATH) as config:
            self._config = json.load(config)

    def get_config(self):
        for configuration in self._config['configurations']:
            if configuration['provider'] == self.EMAIL_PROVIDER:
                return configuration

    def get_event(self, event_name: str):
        return self._config['events'][event_name]

    @property
    def SOURCE_EMAIL(self):
        return self._config.get("sourceEmail")

    @property
    def ERROR_REPORTING_EMAIL(self):
        return self._config.get('errorReportingEmail')


class MailjetConfig(Config):
    MAILJET_API_KEY: str
    MAILJET_API_SECRET: str
    MAILJET_API_VERSION: str = 'v3.1'


class SESConfig(Config):
    pass


config_classes = [
    MailjetConfig,
    SESConfig
]


class EmailConfig(*config_classes):
    pass
