from .base_model import BaseModel
from .event_model import EventModel
from entity import Ticket, Event, Order

class TicketModel(BaseModel):
    def __init__(self):
        """Fungsi constructor dari class CategoryModel yang digunakan untuk memanggil constructor parent class
        dan mengisi properti _tabel dengan nama tabel.
        """
        super(TicketModel, self).__init__()
        self._table = 'ticket'

    def get_event_tickets(self, events: list[Event]) -> list[Event]:
        """Fungsi get_event_tickets digunakan untuk mengambil data ticket dari events.

        Args:
            events (list[Event]): list dari object Event

        Returns:
            list[Event]: list dari object Event
        """
        # cek jika events kosong maka return events
        if not events:
            return events
        
        # for loop untuk setiap event
        for event in events:
            # membuat kondisi where
            condition = f'event_id = {event.get_id()}'
            # mengambil data tiket sesuai kondisi where
            tickets = self.get_where(condition)
            # pparsing tickets agar menjadi list dari object Ticket
            tickets = self.parseList(tickets)
            # set tickets untuk event
            event.set_tickets(tickets)
        return events

    def get_order_ticket(self, orders: list[Order]) -> list[Order]:
        """Fungsi get_order_ticket digunakan untuk mengambil data ticket dari orders.

        Args:
            orders (list[Order]): list dari object Order

        Returns:
            list[Order]: list dari object Order
        """
        # inisiasi model event
        event_model = EventModel()

        # cek jika orders kosong maka return orders
        if not orders:
            return orders
        
        # for loop untuk setiap event
        for order in orders:
            # membuat kondisi where
            condition = f'id = {order.get_ticket_id()}'
            # mengambil satu ticket sesuai dengan kondisi where
            ticket = self.get_where(condition)[0]
            # parsing ticket agar menjadi object dari Ticket
            ticket = self.parse(ticket)
            # set ticket untuk order
            order.set_ticket(ticket)

            # membuat kondisi where
            condition = f"id = {ticket.get_event_id()}"
            # ambil satu event sesuai dengan kondisi where
            event = event_model.get_where(condition)[0]
            # parsing event agar menjadi object dari Event
            event = event_model.parse(event)
            # set event untuk order
            order.set_event(event)
        return orders

    def parse(self, data: dict) -> Ticket:
        """Fungsi parse digunakan untuk mengubah data hasil query yang berupa dictionary menjadi object.

        Args:
            data (dict): data hasil query berupa dictionary

        Returns:
            Ticket: object dari class Ticket
        """
        return Ticket(**data)

    def parseList(self, data: list[dict]) -> list[Ticket]:
        """Fungsi parseList digunakan untuk mengubah data hasil query yang berupa list dari dictionary menjadi list dari object.

        Args:
            data (list[dict]): list / array dari hasil query

        Returns:
            list[Ticket]: list / array dari object class Ticket
        """
        result = []
        for item in data:
            result.append(Ticket(**item))
        return result