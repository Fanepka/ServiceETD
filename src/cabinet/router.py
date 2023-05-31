from fastapi import APIRouter

from cabinet.db_queries import RequestQuery
from cabinet.schemas import Request


router = APIRouter()
rq = RequestQuery()


@router.get("/requests")
async def requests(limit: int = 25) -> list[Request]:
    rqs = await rq.get_all(limit)

    return rqs

