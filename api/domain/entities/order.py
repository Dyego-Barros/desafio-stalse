from pydantic import BaseModel
from typing import Optional


class Order(BaseModel):
    order_id: Optional[str] | None = None
    order_status: str
    priority: str
    
    model_config={
        "from_attributes": True
    }



class OrderUpdate(BaseModel):
    order_status: Optional[str] = None
    priority: Optional[str] = None