from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.config import get_settings

settings = get_settings()


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:
    print(f"--- Using {settings.env} settings ---")  # noqa: T201
    yield


app = FastAPI(lifespan=lifespan)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=settings.cors_methods,
    allow_headers=["*"],
)


@app.get("/health")
def get_health() -> dict[str, str]:
    return {"status": "ok"}
