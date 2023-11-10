from enum import StrEnum, auto


class EmailService(StrEnum):
    mailjet = auto()
    ses = auto()
