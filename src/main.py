from fastapi import FastAPI
from cabinet.router import router




app = FastAPI()

app.include_router(
    router,
    tags=["Requests"]
)
