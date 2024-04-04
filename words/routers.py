from fastapi import APIRouter

from .counter import count_words
from .models import CountTextWordsPayload


router = APIRouter(prefix="/words", tags=["words"])


@router.post("/count")
async def count_text_words(payload: CountTextWordsPayload):
    return {"count": count_words(payload.text)}
