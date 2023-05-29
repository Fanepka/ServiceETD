from pydantic import BaseModel


class Executer(BaseModel):

    id: int
    fullname: str