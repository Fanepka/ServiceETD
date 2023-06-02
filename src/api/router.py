import json

from fastapi import APIRouter

from api.db_queries import *
from api.schemas import *


router = APIRouter(
    prefix="",
    tags=["Requests"]
)
rq = RequestQuery()
aq = AddreasQuery()
cq = CompanyQuery()
eq = ExecuterQuery()
sq = SystemQuery()
tq = TypeQuery()


#Requests

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

@router.delete("/requests/{request_id}")
async def delete_request_by_id(request_id: int):
    request = await rq.get(request_id)
    if not request:
        return {"error": {"Request not found"}}
    
    await rq.delete(request_id)
    return {"msg": {"status": "success"}}


#TODO: Подумать над тем, куда запихнуть остальные маршруты


#Addreases
@router.get("/addreases")
async def requests(limit: int = 25) -> list[Addreas]:
    rqs = await aq.get_all(limit)

    return rqs

@router.get("/addreases/{addr_id}")
async def request_by_id(addr_id: int):
    request = await aq.get(addr_id)
    if not request:
        return {"error": {"Addreas not found"}}

    return request

@router.delete("/addreases/{addr_id}")
async def delete_request_by_id(addr_id: int):
    request = await aq.get(addr_id)
    if not request:
        return {"error": {"Addreas not found"}}
    
    await aq.delete(addr_id)
    return {"msg": {"status": "success"}}


#Company
@router.get("/companies")
async def requests(limit: int = 25) -> list[Company]:
    rqs = await rq.get_all(limit)

    return rqs

@router.get("/companies/{addr_id}")
async def request_by_id(addr_id: int):
    request = await rq.get(addr_id)
    if not request:
        return {"error": {"Addreas not found"}}

    return request

@router.delete("/companies/{addr_id}")
async def delete_request_by_id(addr_id: int):
    request = await rq.get(addr_id)
    if not request:
        return {"error": {"Addreas not found"}}
    
    await rq.delete(addr_id)
    return {"msg": {"status": "success"}}



    
    
