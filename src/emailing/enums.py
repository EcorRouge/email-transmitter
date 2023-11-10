from enum import Enum


class EmailServiceProvider(str, Enum):
    mailjet = 'mailjet'
    ses = 'ses'

    def __str__(self):
        return str(self.value)
