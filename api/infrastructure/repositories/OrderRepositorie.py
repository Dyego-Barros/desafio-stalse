from domain.interface.Iorder import IOrder
from sqlalchemy.orm import Session
from domain.entities.order import Order,OrderUpdate
from infrastructure.models.OrderModel import ModelOrder
from pathlib import Path
import json

PROJECT_ROOT = Path(__file__).resolve().parents[3]
METRICS_DIR = PROJECT_ROOT / "data" / "processed"

class OrderRepositories(IOrder):
    
    def __init__(self, db:Session):
        self.__db = db
        
    
    
    def get_all_tickets(self)->list[Order]:
        try:
            data = self.__db.query(ModelOrder).all()
            dados = [Order.model_validate(dado) for dado in data]
            return [Order.model_dump(dado) for dado in dados]
        except Exception as error:
            print(error)
            
    
    def get_metrics(self):
        try:
            data = open(f"{METRICS_DIR}/metrics.json").read()
            return json.loads(data)
        except Exception as error:
            print(error)
            
    def get_ticket_id(self, id:str)-> Order:
        try:
            data = self.__db.query(ModelOrder).filter(ModelOrder.order_id == id).first()
            dado = Order.model_validate(data)
            return Order.model_dump(dado)
        except Exception as error:
            print(error)
            
    def ticket_update(self, id:str, order:OrderUpdate)->bool:
        try:
            self.__db.query(ModelOrder).filter(ModelOrder.order_id == id).update({
             ModelOrder.order_status: order.order_status,
             ModelOrder.priority: order.priority
            })
            self.__db.commit()
            return True
        except Exception as error:
            self.__db.rollback()
            print(error)
            return False