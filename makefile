# Defina a versão do Python para ser usada em todo o projeto
PYTHON_VERSION ?= 3.8.10
# Diretórios que contêm os módulos da biblioteca que este repositório constrói
LIBRARY_DIRS = mylibrary
# Diretório de artefatos de build organizados neste Makefile
BUILD_DIR ?= build

# Opções para o PyTest
PYTEST_HTML_OPTIONS = --html=$(BUILD_DIR)/report.html --self-contained-html
PYTEST_TAP_OPTIONS = --tap-combined --tap-outdir $(BUILD_DIR)
PYTEST_COVERAGE_OPTIONS = --cov=$(LIBRARY_DIRS)
PYTEST_OPTIONS ?= $(PYTEST_HTML_OPTIONS) $(PYTEST_TAP_OPTIONS) $(PYTEST_COVERAGE_OPTIONS)

# Opções de verificação de tipos para o MyPy
MYPY_OPTS ?= --python-version $(basename $(PYTHON_VERSION)) --show-column-numbers --pretty --html-report $(BUILD_DIR)/mypy
# Arquivos de instalação do Python
PYTHON_VERSION_FILE=.python-version
ifeq ($(shell which pyenv),)
# Se o pyenv não estiver instalado, adivinhe o caminho final, caso seja útil
PYENV_VERSION_DIR ?= $(HOME)/.pyenv/versions/$(PYTHON_VERSION)
else
# Se o pyenv estiver instalado, use o caminho correto
PYENV_VERSION_DIR ?= $(shell pyenv root)/versions/$(PYTHON_VERSION)
endif
# Defina o comando para o gerenciador de pacotes pip
PIP ?= pip3

# Configurações para o Poetry
POETRY_OPTS ?=
POETRY ?= poetry $(POETRY_OPTS)
# Executa um binário Python usando o Poetry
RUN_PYPKG_BIN = $(POETRY) run

# Cores para mensagens de terminal
COLOR_ORANGE = \033[33m
COLOR_RESET = \033[0m

##@ Utilitários

.PHONY: help
help:  ## Exibe esta ajuda
	@awk 'BEGIN {FS = ":.*##"; printf "\nUso:\n  make \033[36m\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

.PHONY: version-python
version-python: ## Exibe a versão do Python em uso
	@echo $(PYTHON_VERSION)

##@ Testes

.PHONY: test
test: ## Executa os testes
	$(RUN_PYPKG_BIN) pytest \
		$(PYTEST_OPTIONS) \
		tests/*.py

##@ Build e Publicação

.PHONY: build
build: ## Executa o build
	$(POETRY) build

.PHONY: publish
publish: ## Publica o build no repositório configurado
	$(POETRY) publish $(POETRY_PUBLISH_OPTIONS_SET_BY_CI_ENV)

.PHONY: deps-py-update
deps-py-update: pyproject.toml ## Atualiza as dependências do Poetry, por exemplo, após adicionar uma nova manualmente
	$(POETRY) update

##@ Configuração
# Detecção dinâmica do diretório de instalação do Python com pyenv
$(PYENV_VERSION_DIR):
	pyenv install --skip-existing $(PYTHON_VERSION)
$(PYTHON_VERSION_FILE): $(PYENV_VERSION_DIR)
	pyenv local $(PYTHON_VERSION)

.PHONY: deps
deps: deps-brew deps-py  ## Instala todas as dependências

.PHONY: deps-brew
deps-brew: Brewfile ## Instala dependências de desenvolvimento via Homebrew
	brew bundle --file=Brewfile
	@echo "$(COLOR_ORANGE)Verifique se o pyenv está configurado no seu shell.$(COLOR_RESET)"
	@echo "$(COLOR_ORANGE)Ele deve ter algo como 'eval \$$(pyenv init -)'$(COLOR_RESET)"

.PHONY: deps-py
deps-py: $(PYTHON_VERSION_FILE) ## Instala dependências de desenvolvimento e runtime do Python
	$(PIP) install --upgrade \
		--index-url $(PYPI_PROXY) \
		pip
	$(PIP) install --upgrade \
                                     		--index-url $(PYPI_PROXY) \
                                     		poetry
	$(POETRY) install

##@ Qualidade de Código

.PHONY: check
check: check-py ## Executa linters e outras ferramentas importantes

.PHONY: check-py
check-py: check-py-flake8 check-py-black check-py-mypy ## Verifica apenas arquivos Python

.PHONY: check-py-flake8
check-py-flake8: ## Executa o linter flake8
	$(RUN_PYPKG_BIN) flake8 .

.PHONY: check-py-black
check-py-black: ## Executa o black em modo de verificação (sem alterações)
	$(RUN_PYPKG_BIN) black --check --line-length 118 --fast .

.PHONY: check-py-mypy
check-py-mypy: ## Executa o mypy
	$(RUN_PYPKG_BIN) mypy $(MYPY_OPTS) $(LIBRARY_DIRS)

.PHONY: format-py
format-py: ## Executa o black e faz alterações quando necessário
	$(RUN_PYPKG_BIN) black .

.PHONY: format-autopep8
format-autopep8: ## Formata o código com o autopep8
	$(RUN_PYPKG_BIN) autopep8 --in-place --recursive .

.PHONY: format-isort
format-isort: ## Ordena as importações com isort
	$(RUN_PYPKG_BIN) isort --recursive .

.PHONY: migrate
migrate: ## Executa as migrações do Django
	docker-compose exec web python manage.py migrate --noinput

.PHONY: seed
seed: ## Executa o seeding de dados
	poetry run python manage.py seed
