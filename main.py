from http import HTTPStatus
from fastapi import FastAPI, Response
from config import lifespan
from routes import candidate_router, user_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(lifespan=lifespan)

app.include_router(candidate_router)
app.include_router(user_router)


@app.get("/health")
def index():
    """Simple health check API"""
    return Response(status_code=HTTPStatus.OK)
