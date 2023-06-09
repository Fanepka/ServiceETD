from fastapi import APIRouter
from fastapi.responses import HTMLResponse

from api.db_queries import UserQuery
from api.schemas import User


router = APIRouter(
    prefix="",
    tags=["Users"]
)
uq = UserQuery()



@router.post("/users", )
async def create_user(user: User):
    await uq.create_user(user.email, user.password)


@router.get("/user/me")
async def me(token: str):
    user = await uq.get_by_token(token)
    if not user:
        return HTMLResponse(content="Not found", status_code=404)

    return HTMLResponse(f"Hello {user.email}")
