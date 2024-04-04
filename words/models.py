from pydantic import BaseModel


class CountTextWordsPayload(BaseModel):
    text: str
