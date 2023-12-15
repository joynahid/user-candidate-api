from http import HTTPStatus
from fastapi import FastAPI, Response
from routes import candidate_router, user_router

app = FastAPI()

app.include_router(candidate_router)
app.include_router(user_router)


@app.get('/health')
def index():
    """Simple health check API"""
    return Response(status_code=HTTPStatus.OK)
