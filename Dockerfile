FROM afeef/rococo_service_processor:latest

WORKDIR /app/src

COPY pyproject.toml poetry.lock* ./

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

COPY ./src ./

ENV PYTHONPATH /app

WORKDIR /app

COPY ./docker-entrypoint.sh ./
RUN chmod +x ./docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh"]
#ENTRYPOINT [ "/bin/bash", "-l", "-c" ]