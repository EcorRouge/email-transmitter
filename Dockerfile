FROM ecorrouge/rococo-service-host

WORKDIR /app/src/services/email_transmitter

COPY pyproject.toml poetry.lock* ./

COPY ./pyproject.toml /app/pyproject.toml

RUN poetry lock --no-update && poetry install

COPY ./src ./src
COPY ./tests ./tests

WORKDIR /app

ENV PYTHONPATH /app

ENV MESSAGING_TYPE=RabbitMqConnection
ENV PROCESSOR_TYPE=EmailServiceProcessor
ENV PROCESSOR_MODULE=services.email_transmitter.src.email_processor

COPY ./docker-entrypoint.sh ./
RUN chmod +x ./docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh", "-l", "-c"]
