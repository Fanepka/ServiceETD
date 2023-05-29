from pydantic import BaseModel
from datetime import datetime


from models.addreas import Addreas
from models.company import Company
from models.executer import Executer
from models.system import System
from models.type import Type




class Ticket(BaseModel):

    id: int
    company: Company
    status: str
    addreas: Addreas
    system: System
    phone: str
    contact: str
    date: datetime
    executer: Executer
    type: Type
    description: str
