from libs.mysql import MySQL
from config import DATABASE

from typing import List

from models.ticket import Ticket


class TicketQuery(MySQL):


    def __init__(self):
        super().__init__(**DATABASE)


    async def insert(self, ticket: Ticket):
        self.cursor(
            "INSERT INTO Tickets(company, status, addreas, system, phone, contact, date, executer, type, description) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (ticket.company, ticket.status, ticket.addreas, ticket.system, ticket.phone, ticket.contact, ticket.date, ticket.executer, ticket.type, ticket.description)
        )
        await self.commit()

    async def fetch_by_id(self, ticket_id: int) -> Ticket:
        self.cursor("SELECT * FROM Tickets WHERE id = %s", (ticket_id, ))
        
        r = await self.fetchone()
        if not r:
            return None
        
        return Ticket(**r)
    
    async def get_all(self) -> List[Ticket]:
        self.cursor("SELECT * FROM Tickets")
        
        r = await self.fetchall()
        if not r:
            return None
        
        return [Ticket(**i) for i in r]