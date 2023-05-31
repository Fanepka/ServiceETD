from config import DATABASE
from database import MySQL
from typing import List

from cabinet.schemas import Request



class RequestQuery(MySQL):


    def __init__(self):
        super().__init__(**DATABASE)


    async def get_all(self, limit: int) -> List[Request]:
        
        self.cursor("SELECT * FROM Requests LIMIT %s", (limit, ))

        return [Request(**i) for i in await self.fetchall()]