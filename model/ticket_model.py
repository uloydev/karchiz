from .base_model import BaseModel

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