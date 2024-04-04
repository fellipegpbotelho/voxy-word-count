from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import FileResponse


app = FastAPI()


class Payload(BaseModel):
    text: str


@app.get("/")
def index():
    return FileResponse("index.html")


@app.post("/words/count")
def count_words(payload: Payload):
    return {"count": len(payload.text.rsplit())}
