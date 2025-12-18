from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from core.database.database import Database
from application.services.OrderService import OrderService
from fastapi import status
from fastapi.responses import JSONResponse
from domain.entities.order import Order,OrderUpdate
#Instãncia do banco de dados, para retornar Session
db = Database()

router = APIRouter(prefix="/desafio", tags=["Desafio Stalse"])

@router.get("/tickets")
def tickets(db:Session = Depends(db.connection)):
    service = OrderService(db=db)
    try:
        tickets = service.get_all_tickets()
        if tickets:            
            return JSONResponse(content=tickets, status_code=status.HTTP_200_OK)
        return JSONResponse(content={"message":"Nenhum ticket foi encontrado"}, status_code=status.HTTP_200_OK)
    except Exception as error:
        print(error)
        return JSONResponse(content={"message":"Desculpa ocorreu um comportamento inesperado!"}, status_code=status.HTTP_400_BAD_REQUEST)
    
@router.get("/metrics")
def metrics(db: Session= Depends(db.connection)):
    service = OrderService(db=db)
    try:
        metrics = service.get_metrics()
        if metrics:
            return JSONResponse(content=metrics, status_code=status.HTTP_200_OK)
        return JSONResponse(content={"message":"Nenhuma metrica foi encontrada"}, status_code=status.HTTP_200_OK)
        
    except Exception as error:
        print(error)
        return JSONResponse(content={"message":"Desculpa ocorreu um comportamento inesperado!"}, status_code=status.HTTP_400_BAD_REQUEST)
    
@router.get("/ticket/{ticket_id}")
def get_ticket_id(ticket_id:str, db:Session=Depends(db.connection)):
    service = OrderService(db=db)
    try:
        ticket = service.get_ticket_id(id=ticket_id)
        if ticket:
            return JSONResponse(content=ticket, status_code=status.HTTP_200_OK)
        return JSONResponse(content={"message":"Nenhum ticket encontrado com o identificadorfornecido"})
    except Exception as error:
        print(error)
        return JSONResponse(content={"message":"Desculpa ocorreu um comportamento inesperado!"}, status_code=status.HTTP_400_BAD_REQUEST)
    
@router.put("/ticket/update/{ticket_id}")
def ticket_update(ticket_id:str, order:OrderUpdate, db:Session=Depends(db.connection)):
    service = OrderService(db=db)
    try:
        update = service.update_ticket(id=ticket_id, order=order)
        if update:
            return JSONResponse(content={"message":"Ticket atualizado com sucesso!"}, status_code=status.HTTP_202_ACCEPTED)
        return JSONResponse(content={"message":"Error ao atualizar ticket"}, status_code=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        print(error)
        return JSONResponse(content={"message":"Desculpa ocorreu um comportamento inesperado!"}, status_code=status.HTTP_400_BAD_REQUEST)
    