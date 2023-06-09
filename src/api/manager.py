from functools import wraps
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from api.db_queries import UserQuery


uq = UserQuery()

def token_required(func):
    @wraps(func)
    async def wrapper(*args, request: Request, **kwargs):
        token = request.headers.get('token')
        user = await uq.get_by_token(token)
        if not user:
            HTMLResponse("Authorization failed", status_code=404)
            return

        return await func(*args, request, **kwargs)
    return wrapper

        