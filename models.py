from pydantic import BaseModel


class WordCountPayload(BaseModel):
    text: str
