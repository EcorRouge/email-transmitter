FROM ecorrouge/rococo-service-host

WORKDIR /app/src/services/email_transmitter

# Copy poetry files
COPY pyproject.toml poetry.lock* ./

# Configure Poetry to install dependencies globally (no virtual environment)
RUN poetry config virtualenvs.create false

# Install ALL dependencies (main + dev) globally in the base image
RUN poetry install --no-root && \
    poetry cache clear --all pypi

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
