from fastapi import APIRouter, Depends

from api.db_queries import AddressQuery
from api.schemas import Address
from api.manager import JWTBearer


router = APIRouter(
    prefix="",
    tags=["Addresses"], 
    dependencies=[Depends(JWTBearer())]
)
aq = AddressQuery()




@router.get("/addresses")
async def addresses(limit: int = 25) -> list[Address]:
    aqs = await aq.get_all(limit)

    return aqs

@router.get("/addresses/{addr_id}")
async def address_by_id(addr_id: int):
    address = await aq.get(addr_id)
    if not address:
        return {"error": {"Address not found"}}

    return address

@router.post("/addresses")
async def create_address(address: Address) -> Address:
    await aq.create(address.name)
    select_address = await aq.select_last_record()
    return select_address

@router.delete("/addresses/{addr_id}")
async def delete_address_by_id(addr_id: int):
    address = await aq.get(addr_id)
    if not address:
        return {"error": {"Address not found"}}
    
    await aq.delete(addr_id)
    return {"msg": {"status": "success"}}