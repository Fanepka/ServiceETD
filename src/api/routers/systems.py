from fastapi import APIRouter, Depends

from api.db_queries import SystemQuery
from api.schemas import System
from api.manager import JWTBearer


router = APIRouter(
    prefix="",
    tags=["Systems"],
    dependencies=[Depends(JWTBearer())]
)
sq = SystemQuery()




@router.get("/systems")
async def systems(limit: int = 25) -> list[System]:
    sqs = await sq.get_all(limit)

    return sqs

@router.get("/systems/{sys_id}")
async def system_by_id(sys_id: int):
    system = await sq.get(sys_id)
    if not system:
        return {"error": {"System not found"}}

    return system

@router.post("/systems")
async def create_system(system: System) -> System:
    await sq.create(system.name)
    select_address = await sq.select_last_record()
    return select_address

@router.delete("/systems/{sys_id}")
async def delete_system_by_id(sys_id: int):
    system = await sq.get(sys_id)
    if not system:
        return {"error": {"System not found"}}
    
    await sq.delete(sys_id)
    return {"msg": {"status": "success"}}