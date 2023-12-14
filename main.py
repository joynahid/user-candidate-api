from http import HTTPStatus
from fastapi import FastAPI
from starlette.responses import Response

from models.user import UserModel

app = FastAPI()


@app.get('/health')
def index():
    """Simple health check API"""
    return Response(status_code=HTTPStatus.OK)

@app.post('/user')
def create_user(user: UserModel):
    """Craete a new user entry to the users collection"""
    return Response(status_code=HTTPStatus.CREATED)
