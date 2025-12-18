from infrastructure.repositories.OrderRepositorie import OrderRepositories
from domain.entities.order import Order,OrderUpdate
from sqlalchemy.orm import Session

class OrderService:
    def __init__(self, db:Session):
        self.__db = db
        self.__repo = OrderRepositories(db=self.__db)
        
    
    def get_all_tickets(self):
        try:
            tickets = self.__repo.get_all_tickets()
            if tickets:
                return tickets
            return []
        except Exception as error:
            print(error)
            return []
        
    def get_metrics(self):
        try:
            metrics = self.__repo.get_metrics()
            if metrics:
                return metrics
            return []
        except Exception as error:
            print(error)
            return []
        
    def get_ticket_id(self, id:str):
        try:
            ticket = self.__repo.get_ticket_id(id=id)
            if ticket:
                return ticket
            return {}
        except Exception as error:
            print(error)
            return {}
        
    def update_ticket(self, id:str, order:OrderUpdate):
        try:
            update = self.__repo.ticket_update(id=id, order=order)
            if update:
                return True
            return False
        except Exception as error:
            print(error)
            return False
        
    