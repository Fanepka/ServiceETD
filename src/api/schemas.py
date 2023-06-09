from pydantic import BaseModel
from datetime import datetime



class User(BaseModel):

    email: str
    password: str
    token: str = None


class Address(BaseModel):

    id: int = None
    name: str


class Company(BaseModel):

    id: int = None
    name: str


class Executer(BaseModel):

    id: int = None
    fullname: str


class System(BaseModel):


    id: int = None
    name: str


class Type(BaseModel):

    id: int = None
    name: str
    days: int


class Request(BaseModel):

    id: int = None
    company: Company | int
    status: str
    addreas: Address | int
    system: System | int
    phone: str
    contact: str
    date: datetime
    executer: Executer | int
    type: Type | int
    description: str
