from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import FileResponse

from models import WordCountPayload

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    print(f"[http_error]: {repr(exc)}")
    return await http_exception_handler(request, exc)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print(f"[client_error]: {exc}")
    return await request_validation_exception_handler(request, exc)


@app.get("/")
async def index():
    return FileResponse("index.html")


@app.post("/words/count")
async def count_words(payload: WordCountPayload):
    return {"count": len(payload.text.rsplit())}
