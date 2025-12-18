from core.database.database import Database
import json
from infrastructure.models.OrderModel import ModelOrder
from sqlalchemy.orm import Session
from pathlib import Path


SEEDS_PATH = Path(__file__).resolve().parent

#Insere seeds no banco, caso nao existam
def insert_seeds(db:Session):
    try:
        seeds = open(f"{SEEDS_PATH}/seeds.json").read()
        seeds = json.loads(seeds)
        for seed in seeds:
           dado = db.query(ModelOrder).filter(ModelOrder.order_id==seed["order_id"]).first()
          
           if not dado:
               db.add(ModelOrder(**seed))
               db.commit()
        
    except Exception as error:
        print(error)
