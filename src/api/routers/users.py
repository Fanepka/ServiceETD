from fastapi import APIRouter, Depends

from api.db_queries import UserQuery
from api.schemas import UserLogging
from api.manager import signJWT


router = APIRouter(
    prefix="",
    tags=["Users"]
)
uq = UserQuery()



@router.post("/users")
async def create_user(user: UserLogging) -> dict:
    token = signJWT(user.email)
    await uq.create_user(user.email, user.password, token['access_token'])

    return token


@router.post("/user/me")
async def me(user: UserLogging):
    user = await uq.get_by_email_and_password(user.email, user.password)
    if not user:
        return {
            "error": "Wrong login details!"
        }

    return signJWT(user.email)
