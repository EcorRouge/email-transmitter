FROM ecorrouge/rococo_service_processor:latest

WORKDIR /app/src/services/emailing

COPY pyproject.toml poetry.lock* ./

RUN poetry install

COPY ./src/emailing ./
COPY ./src/config.json ./

WORKDIR /app

COPY ./tests/test_queue.py ./tests/test_queue.py

ENV PYTHONPATH /app

COPY ./docker-entrypoint.sh ./
RUN chmod +x ./docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh", "-l", "-c"]
#ENTRYPOINT [ "/bin/bash", "-l", "-c" ]
