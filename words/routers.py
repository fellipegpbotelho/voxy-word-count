from fastapi import APIRouter

from .models import WordCountPayload


router = APIRouter(prefix="/words", tags=["words"])


@router.post("/count")
async def count_words(payload: WordCountPayload):
    return {"count": len(payload.text.rsplit())}
