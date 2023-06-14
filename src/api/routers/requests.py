from fastapi import APIRouter, Depends

from api.db_queries import *
from api.schemas import *
from api.manager import JWTBearer


router = APIRouter(
    prefix="",
    tags=["Requests"],
    dependencies=[Depends(JWTBearer())]
)
rq = RequestQuery()



@router.get("/requests")
async def requests(limit: int = 25) -> list[Request]:
    rqs = await rq.get_all(limit)

    return rqs

@router.get("/requests/{request_id}")
async def request_by_id(request_id: int):
    request = await rq.get(request_id)
    if not request:
        return {"error": {"Request not found"}}

    return request

#TODO: Дописать логику работы 
@router.post("/requests")
async def create_request(request: Request) -> Request:
    await rq.create(
        request.company, request.addreas, request.status, request.system, request.phone,
        request.contact, request.date, request.executer, request.type, request.description
    )
    select_address = await rq.select_last_record()
    return select_address

@router.delete("/requests/{request_id}")
async def delete_request_by_id(request_id: int):
    request = await rq.get(request_id)
    if not request:
        return {"error": {"Request not found"}}
    
    await rq.delete(request_id)
    return {"msg": {"status": "success"}}