from .base_model import BaseModel
from .event_model import EventModel

class TicketModel(BaseModel):
    def __init__(self):
        super(TicketModel, self).__init__()
        self._table = 'ticket'

    def get_event_tickets(self, events: list) -> list:
        if not events:
            return events
        for event in events:
            condition = f'event_id = {event["id"]}'
            event['tickets'] = self.get_where(condition)
        return events

    def get_order_ticket(self, orders: list) -> list:
        event_model = EventModel()
        if not orders:
            return orders
        for order in orders:
            condition = f'id = {order["ticket_id"]}'
            ticket = self.get_where(condition)[0]
            order['ticket'] = ticket
            event = event_model.get_where(f"id = {ticket['event_id']}")[0]
            order['event'] = event
        return orders