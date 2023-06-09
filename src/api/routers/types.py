from fastapi import APIRouter

from api.db_queries import TypeQuery
from api.schemas import Type


router = APIRouter(
    prefix="",
    tags=["Types"]
)
tq = TypeQuery()




@router.get("/types")
async def types(limit: int = 25) -> list[Type]:
    tqs = await tq.get_all(limit)

    return tqs

@router.get("/types/{type_id}")
async def type_by_id(type_id: int):
    tps = await tq.get(type_id)
    if not tps:
        return {"error": {"Type not found"}}

    return tps

@router.post("/types")
async def create_company(tp: Type) -> Type:
    await tq.create(tp.name, tp.days)
    select_address = await tq.select_last_record()
    return select_address

@router.delete("/types/{type_id}")
async def delete_type_by_id(type_id: int):
    tps = await tq.get(type_id)
    if not tps:
        return {"error": {"Type not found"}}
    
    await tq.delete(type_id)
    return {"msg": {"status": "success"}}