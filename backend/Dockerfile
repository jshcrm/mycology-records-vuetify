FROM python:3.10-slim

RUN apt-get update \
	&& apt-get install -y \
    curl \
	# psycopg
	gcc libpq-dev

RUN apt-get update --fix-missing

# Doppler
RUN apt-get install -y apt-transport-https ca-certificates curl gnupg && \
    curl -sLf --retry 3 --tlsv1.2 --proto "=https" 'https://packages.doppler.com/public/cli/gpg.DE2A7741A397C129.key' | apt-key add - && \
    echo "deb https://packages.doppler.com/public/cli/deb/debian any-version main" | tee /etc/apt/sources.list.d/doppler-cli.list && \
    apt-get update && \
    apt-get -y install doppler

RUN mkdir /poetry

ENV POETRY_HOME=/etc/poetry PATH="/etc/poetry/bin:${PATH}" PYTHONPATH=${PYTHONPATH}:/backend

RUN python -m pip install --upgrade pip \
	&& python -m pip install --upgrade setuptools \
    && curl -sSL https://install.python-poetry.org | python

COPY ./pyproject.toml /poetry
COPY ./poetry.lock /poetry

RUN cd /poetry \
    && poetry config virtualenvs.create false \
	&& poetry update \
    && poetry install

RUN mkdir /backend

COPY ./ /backend

COPY ./run.sh /

CMD ["/run.sh"]
