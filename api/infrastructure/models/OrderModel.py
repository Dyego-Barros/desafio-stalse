from sqlalchemy import Column,String
from core.database.database import Base


class ModelOrder(Base):
    __tablename__= "orders"
    
    order_id = Column(String, primary_key=True, index=True)
    order_status = Column(String, nullable=False)
    priority = Column(String, nullable=False)