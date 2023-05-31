from pydantic import BaseModel
from datetime import datetime


class Addreas(BaseModel):

    id: int
    name: str


class Company(BaseModel):

    id: int
    name: str


class Executer(BaseModel):

    id: int
    fullname: str


class System(BaseModel):


    id: int
    name: str


class Type(BaseModel):

    id: int
    name: str
    days: int


class Request(BaseModel):

    id: int
    company: Company | int
    status: str
    addreas: Addreas | int
    system: System | int
    phone: str
    contact: str
    date: datetime
    executer: Executer | int
    type: Type | int
    description: str
