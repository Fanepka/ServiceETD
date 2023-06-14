from fastapi import APIRouter, Depends

from api.db_queries import CompanyQuery
from api.schemas import Company
from api.manager import JWTBearer

router = APIRouter(
    prefix="",
    tags=["Companies"],
    dependencies=[Depends(JWTBearer())]
)
cq = CompanyQuery()




@router.get("/companies")
async def companies(limit: int = 25) -> list[Company]:
    cqs = await cq.get_all(limit)

    return cqs

@router.get("/companies/{comp_id}")
async def company_by_id(comp_id: int):
    company = await cq.get(comp_id)
    if not company:
        return {"error": {"Company not found"}}

    return company

@router.post("/companies")
async def create_company(comp: Company) -> Company:
    await cq.create(comp.name)
    select_address = await cq.select_last_record()
    return select_address

@router.delete("/companies/{comp_id}")
async def delete_company_by_id(comp_id: int):
    company = await cq.get(comp_id)
    if not company:
        return {"error": {"Company not found"}}
    
    await cq.delete(comp_id)
    return {"msg": {"status": "success"}}