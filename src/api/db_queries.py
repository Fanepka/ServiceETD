from config import DATABASE
from database import MySQL
from typing import List

from api.schemas import *



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
    
    async def delete(self, request_id: int):
        self.cursor("DELETE FROM Requests WHERE id = %s", (request_id, ))
        await self.commit()


class AddreasQuery(MySQL):


    def __init__(self):
        super().__init__(**DATABASE)


    async def get_all(self, limit: int) -> List[Addreas]:
        self.cursor("SELECT * FROM Addreases LIMIT %s", (limit, ))

        return [Addreas(**i) for i in await self.fetchall()]
    
    async def get(self, addr_id: int) -> Addreas:
        self.cursor("SELECT * FROM Addreases WHERE id = %s", (addr_id, ))

        response = await self.fetchone()
        if not response:
            return None
        
        return Addreas(**response)
    
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
    
    async def delete(self, type_id: int):
        self.cursor("DELETE FROM Types WHERE id = %s", (type_id, ))
        await self.commit()
