# hexatron
[![CI](https://github.com/adamwojt/hexatron/workflows/ci/badge.svg?branch=master&event=push)](https://github.com/adamwojt/hexatron/actions)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://timothycrosley.github.io/isort/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)[![pylint](https://img.shields.io/badge/linter-pylint-purple)](https://www.pylint.org/)[![pylint](https://img.shields.io/badge/typing-mypy-blue)](https://mypy.readthedocs.io/en/stable/)

API and CLI to convert decimals to hexadecimals. Employment task.
## Prerequisites
Python >= `3.6.13`

## Running with poetry

1. Follow [instructions to install poetry](https://python-poetry.org/docs/)
2. `git clone https://github.com/adamwojt/hexatron`
3. `cd hexatron`
4. `poetry install`
5. get in `poetry shell` or run commands with `poetry run hexatron [command]`


## CLI
```
Usage: hexatron [OPTIONS] COMMAND [ARGS]...

Commands:
  server [PORT]     Run API server on specified port (default 8080)
  convert [NUMBER]  Convert integer to hexadecimal string
```
#### Commands:
```
hexatron server 5050
> Uvicorn running on http://0.0.0.0:5050 (Press CTRL+C to quit)
```

```
hexatron convert 590
> 24E
```

## API endpoints
- GET `/` and `/docs` : swagger UI, documentation and schema
- GET `/to_hexadecimal/{number}` : convert number to hexadecimal string
- GET `/healthcheck` : Check server is healthy

## Development and testing
- Run tests with `poetry run pytest`
- Install linting with `pre-commit install`
- Run linting with `pre-commit run -a`
- Linters are - `black`, `bandit`, `pylint`, `isort` and `mypy`
- Server should reload on code changes by default
- Github Actions are used as CI that run tests, lint and check server health.
