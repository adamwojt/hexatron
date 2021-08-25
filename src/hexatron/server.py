import uvicorn


def start_server(port):
    uvicorn.run("hexatron.api:app", host="0.0.0.0", port=port, reload=True)
