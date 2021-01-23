from .base_model import BaseModel
from .event_model import EventModel
from entity import Ticket, Event

class TicketModel(BaseModel):
    def __init__(self):
        super(TicketModel, self).__init__()
        self._table = 'ticket'

    def get_event_tickets(self, events: list[Event]) -> list[Event]:
        if not events:
            return events
        for event in events:
            condition = f'event_id = {event.get_id()}'
            tickets = self.get_where(condition)
            tickets = self.parseList(tickets)
            event.set_tickets(tickets)
        return events

    def get_order_ticket(self, orders: list) -> list:
        event_model = EventModel()
        if not orders:
            return orders
        for order in orders:
            condition = f'id = {order.get_ticket_id()}'
            ticket = self.get_where(condition)[0]
            ticket = self.parse(ticket)
            order.set_ticket(ticket)
            event = event_model.get_where(f"id = {ticket.get_event_id()}")[0]
            event = event_model.parse(event)
            order.set_event(event)
        return orders

    def parse(self, data: dict) -> Ticket:
        return Ticket(**data)

    def parseList(self, data: list[dict]) -> list[Ticket]:
        result = []
        for item in data:
            result.append(Ticket(**item))
        return result