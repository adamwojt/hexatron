# hexatron

API and CLI to convert decimals to hexadecimals.
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
- Server should reload on code changes by default
- Github Actions are used as CI that run tests, lint and check server health.
- 
