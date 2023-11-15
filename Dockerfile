FROM ecorrouge/rococo-service-host

WORKDIR /app/src/services/email_transmitter

COPY pyproject.toml poetry.lock* ./

RUN poetry install

COPY ./src ./src
COPY ./tests ./tests

WORKDIR /app

ENV PYTHONPATH /app

COPY ./docker-entrypoint.sh ./
RUN chmod +x ./docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh", "-l", "-c"]
