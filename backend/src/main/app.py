from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from main import settings
from documents.routers import router as documents_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=settings.ALLOW_CREDENTIALS,
    allow_methods=settings.ALLOW_METHODS,
    allow_headers=settings.ALLOW_HEADERS
)

app.include_router(documents_router, prefix='/documents', tags=['Documents'])

