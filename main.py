from http import HTTPStatus
from fastapi import FastAPI
from starlette.responses import Response

app = FastAPI()


@app.get('/health')
def index():
    """Simple health check API"""
    return Response(status_code=HTTPStatus.OK)
