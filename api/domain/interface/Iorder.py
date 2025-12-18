from abc import ABC, abstractmethod
from domain.entities.order import Order, OrderUpdate

class IOrder(ABC):
    
    
    @abstractmethod
    def get_all_tickets(self)-> list[Order]:
        raise NotImplementedError
    
    @abstractmethod
    def get_ticket_id(self,id:int)->Order:
        raise NotImplementedError
    
    @abstractmethod
    def ticket_update(self, id:int, order:OrderUpdate)->bool:
        raise NotImplementedError
    
    @abstractmethod
    def get_metrics(self)->dict:
        raise NotImplementedError