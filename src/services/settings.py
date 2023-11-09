from pydantic import BaseSettings


class Settings(BaseSettings):
    SOURCE_EMAIL: str
    ERROR_REPORTING_EMAIL: str
    CONFIG_JSON_PATH: str

    @staticmethod
    def get_event(event_name: str):
        return event_name


class MailjetSettings(Settings):
    SERVICE_NAME: str = 'mailjet'
    MAILJET_API_KEY: str
    MAILJET_API_SECRET: str
    MAILJET_API_VERSION: str = 'v3.1'


class SESSettings(Settings):
    pass


settings_classes = [MailjetSettings, SESSettings]


class EmailSettings(*settings_classes):
    pass
