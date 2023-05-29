from fastapi import FastAPI
from models.ticket import Ticket

from libs.query import TicketQuery
from typing import List

app = FastAPI()
tq = TicketQuery()


@app.post("/ticket/")
async def create_ticket(ticket: Ticket):
    await tq.insert(ticket)

    return ticket

@app.get("/tickets", response_class=List[Ticket])
async def get_tickets():
    tickets = await tq.get_all()

    return tickets

@app.get("/ticket/{id}")
async def get_ticket_by_id(id: int):
    ticket = await tq.fetch_by_id(id)

    return ticket