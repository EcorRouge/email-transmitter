from factories import email_factory

if __name__ == "__main__":
    settings = {
        'MAILJET_API_KEY': 'fake_api_key',
        'MAILJET_API_SECRET': 'fake_api_secret'
    }

    mailjet_service = email_factory.get('mailjet', **settings)
