from fastapi import FastAPI
from api import rts



app = FastAPI()

for router in rts:
    app.include_router(
    router,
    prefix="/api",
    )

