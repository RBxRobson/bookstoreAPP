FROM python:3.8.1-slim as python-base

# Configurações do ambiente Python e pip
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.0.3 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# Adiciona poetry e venv ao PATH
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Instala dependências essenciais para o Poetry e build do Python
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential

# Instala o Poetry
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

# Instala dependências do Postgres
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

# Define o diretório de trabalho e copia arquivos de dependências do projeto
WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

# Instala dependências de runtime
RUN poetry install --no-dev

# Instala dependências adicionais
RUN poetry install

# Define diretório de trabalho da aplicação
WORKDIR /app

# Copia o código-fonte para o diretório de trabalho
COPY . /app/

# Expõe a porta 8000
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
