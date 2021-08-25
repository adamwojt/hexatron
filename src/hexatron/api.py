from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse

from hexatron.hexatron import to_hexadecimal

app = FastAPI()


@app.get("/", include_in_schema=False)
async def docs_redirect() -> RedirectResponse:
    return RedirectResponse(url="/docs")


@app.get("/to_hexadecimal/{number}")
async def to_hexadecimal_api(number: int) -> str:
    return to_hexadecimal(number)


@app.get("/healthcheck", status_code=status.HTTP_200_OK)
def perform_healthcheck() -> dict:
    """
    Simple route for the GitHub Actions to healthcheck on.
    """
    return {"healthcheck": "Everything OK!"}
