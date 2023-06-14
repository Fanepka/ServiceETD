from fastapi import APIRouter, Depends

from api.db_queries import ExecuterQuery
from api.schemas import Executer   
from api.manager import JWTBearer 


router = APIRouter(
    prefix="",
    tags=["Executer"],
    dependencies=[Depends(JWTBearer())]
)
eq = ExecuterQuery()



@router.get("/executer")
async def executer(limit: int = 25) -> list[Executer]:
    eqs = await eq.get_all(limit)

    return eqs

@router.get("/executer/{exec_id}")
async def executer_by_id(exec_id: int):
    executer = await eq.get(exec_id)
    if not executer:
        return {"error": {"Executer not found"}}

    return executer

@router.post("/executer")
async def create_company(exec: Executer) -> Executer:
    await eq.create(exec.fullname)
    select_address = await eq.select_last_record()
    return select_address

@router.delete("/executer/{exec_id}")
async def delete_executer_by_id(exec_id: int):
    executer = await eq.get(exec_id)
    if not executer:
        return {"error": {"Executer not found"}}
    
    await eq.delete(exec_id)
    return {"msg": {"status": "success"}}