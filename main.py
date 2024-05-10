from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware

from settings import settings
from src.routers import router

app = FastAPI(
    debug=False,
    title="test",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SessionMiddleware,
                    secret_key=settings.SESSION_SECRET_KEY,
                    session_cookie=settings.SESSION_COOKIE_NAME,
                    max_age=3600 * 3)


app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/data", StaticFiles(directory="data"), name="data")
app.include_router(router)