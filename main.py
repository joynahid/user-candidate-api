from http import HTTPStatus
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from config import lifespan
from routes import candidate_router, user_router
from dotenv import load_dotenv


load_dotenv()

app = FastAPI(
    title="Elevatus UserCandidateAPI",
    description="FastAPI based candidate user CRUD API. Login first to use the candidate APIs",
    lifespan=lifespan,
)

app.include_router(candidate_router)
app.include_router(user_router)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8181",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    """Simple health check API"""
    return Response(status_code=HTTPStatus.OK)
