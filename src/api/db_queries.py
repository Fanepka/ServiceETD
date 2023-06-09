from config import DATABASE
from database import MySQL
from typing import List
from datetime import datetime

from api.schemas import *
from api.utils import get_hashed_password, get_token


class UserQuery(MySQL):

    def __init__(self):
        super().__init__(**DATABASE)

    async def create_user(self, email: str, password: str):
        hashed_password = get_hashed_password(password)
        self.cursor(
            "INSERT INTO Users(email, password, token) VALUES(%s, %s, %s)",
            (email, hashed_password, get_token(hashed_password))
        )
        await self.commit()

    async def get_by_token(self, token: str) -> User:
        self.cursor(
            "SELECT * FROM Users WHERE token = %s",
            (token, )
        )

        response = await self.fetchone()
        if not response:
            return None
        
        return User(**response)
        


class RequestQuery(MySQL):


    def __init__(self):
        super().__init__(**DATABASE)


    async def get_all(self, limit: int) -> List[Request]:
        self.cursor("SELECT * FROM Requests LIMIT %s", (limit, ))

        return [Request(**i) for i in await self.fetchall()]
    
    async def get(self, request_id: int) -> Request:
        self.cursor("SELECT * FROM Requests WHERE id = %s", (request_id, ))

        response = await self.fetchone()
        if not response:
            return None
        
        return Request(**response)
    
    async def create(self, company: int, address: int, status: str, system: int, phone: int, contact: str, date: datetime, executer: int, tp: int, description: str):
        self.cursor(
            "INSERT INTO Requests(company, address, status, system, phone, contact, date, executer, type, description) VALUE(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (company, address, status, system, phone, contact, date, executer, tp, description)
            )
        await self.commit()

    async def select_last_record(self) -> Company:
        self.cursor("SELECT * FROM Requests ORDER BY ID DESC LIMIT 1")
        response = await self.fetchone()

        return Request(**response)
    
    async def delete(self, request_id: int):
        self.cursor("DELETE FROM Requests WHERE id = %s", (request_id, ))
        await self.commit()


class AddressQuery(MySQL):


    def __init__(self):
        super().__init__(**DATABASE)


    async def get_all(self, limit: int) -> List[Address]:
        self.cursor("SELECT * FROM Addreases LIMIT %s", (limit, ))

        return [Address(**i) for i in await self.fetchall()]
    
    async def create(self, name: str):
        self.cursor("INSERT INTO Addresses(name) VALUE(%s)", (name, ))
        await self.commit()

    async def select_last_record(self) -> Address:
        self.cursor("SELECT * FROM Addresses ORDER BY ID DESC LIMIT 1")
        response = await self.fetchone()
        
        return Address(**response)
    
    async def get(self, addr_id: int) -> Address:
        self.cursor("SELECT * FROM Addreases WHERE id = %s", (addr_id, ))

        response = await self.fetchone()
        if not response:
            return None
        
        return Address(**response)
    
    async def delete(self, addr_id: int):
        self.cursor("DELETE FROM Addreases WHERE id = %s", (addr_id, ))
        await self.commit()

class CompanyQuery(MySQL):


    def __init__(self):
        super().__init__(**DATABASE)


    async def get_all(self, limit: int) -> List[Company]:
        self.cursor("SELECT * FROM Companies LIMIT %s", (limit, ))

        return [Company(**i) for i in await self.fetchall()]
    
    async def get(self, comp_id: int) -> Company:
        self.cursor("SELECT * FROM Companies WHERE id = %s", (comp_id, ))

        response = await self.fetchone()
        if not response:
            return None
        
        return Company(**response)
    
    async def create(self, name: str):
        self.cursor("INSERT INTO Companies(name) VALUE(%s)", (name, ))
        await self.commit()

    async def select_last_record(self) -> Company:
        self.cursor("SELECT * FROM Companies ORDER BY ID DESC LIMIT 1")
        response = await self.fetchone()

        return Company(**response)
    
    async def delete(self, comp_id: int):
        self.cursor("DELETE FROM Companies WHERE id = %s", (comp_id, ))
        await self.commit()


class ExecuterQuery(MySQL):


    def __init__(self):
        super().__init__(**DATABASE)


    async def get_all(self, limit: int) -> List[Executer]:
        self.cursor("SELECT * FROM Executer LIMIT %s", (limit, ))

        return [Executer(**i) for i in await self.fetchall()]
    
    async def get(self, exec_id: int) -> Executer:
        self.cursor("SELECT * FROM Executer WHERE id = %s", (exec_id, ))

        response = await self.fetchone()
        if not response:
            return None
        
        return Executer(**response)
    
    async def create(self, fullname: str):
        self.cursor("INSERT INTO Executer(fullname) VALUE(%s)", (fullname, ))
        await self.commit()

    async def select_last_record(self) -> Executer:
        self.cursor("SELECT * FROM Executer ORDER BY ID DESC LIMIT 1")
        response = await self.fetchone()

        return Executer(**response)
    
    async def delete(self, exec_id: int):
        self.cursor("DELETE FROM Executer WHERE id = %s", (exec_id, ))
        await self.commit()



class SystemQuery(MySQL):


    def __init__(self):
        super().__init__(**DATABASE)


    async def get_all(self, limit: int) -> List[System]:
        self.cursor("SELECT * FROM Systems LIMIT %s", (limit, ))

        return [System(**i) for i in await self.fetchall()]
    
    async def get(self, sys_id: int) -> System:
        self.cursor("SELECT * FROM Systems WHERE id = %s", (sys_id, ))

        response = await self.fetchone()
        if not response:
            return None
        
        return System(**response)
    
    async def create(self, name: str):
        self.cursor("INSERT INTO Systems(name) VALUE(%s)", (name, ))
        await self.commit()

    async def select_last_record(self) -> System:
        self.cursor("SELECT * FROM Systems ORDER BY ID DESC LIMIT 1")
        response = await self.fetchone()

        return System(**response)
    
    async def delete(self, sys_id: int):
        self.cursor("DELETE FROM Systems WHERE id = %s", (sys_id, ))
        await self.commit()


class TypeQuery(MySQL):


    def __init__(self):
        super().__init__(**DATABASE)


    async def get_all(self, limit: int) -> List[Type]:
        self.cursor("SELECT * FROM Types LIMIT %s", (limit, ))

        return [Type(**i) for i in await self.fetchall()]
    
    async def get(self, type_id: int) -> Type:
        self.cursor("SELECT * FROM Types WHERE id = %s", (type_id, ))

        response = await self.fetchone()
        if not response:
            return None
        
        return Type(**response)
    
    async def create(self, name: str, days: int):
        self.cursor("INSERT INTO Types(name, days) VALUE(%s, %s)", (name, days))
        await self.commit()

    async def select_last_record(self) -> Type:
        self.cursor("SELECT * FROM Types ORDER BY ID DESC LIMIT 1")
        response = await self.fetchone()

        return Type(**response)
    
    async def delete(self, type_id: int):
        self.cursor("DELETE FROM Types WHERE id = %s", (type_id, ))
        await self.commit()
