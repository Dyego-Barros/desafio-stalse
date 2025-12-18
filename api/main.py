from fastapi import FastAPI
from interface.router.OrderRouter import router
from core.database.database import Base, engine, SessionLocal
from contextlib import asynccontextmanager
from core.seeds.loadSeeds import insert_seeds


@asynccontextmanager
async  def lifespan(app:FastAPI):
    Base.metadata.create_all(engine)
    
    db = SessionLocal()
    try:
        insert_seeds(db=db)
    except Exception as error:
        print(error)
    finally:
        
        yield
    

app = FastAPI(title="Desafio Stalse",debug=True,summary="API para gerenciamento de pedidos e tickets", description="""
API responsável por gerenciar pedidos, tickets e prioridades.

### Funcionalidades
- Criar pedidos
- Consultar tickets
- Atualizar status
- Integração com sistemas externos

### Autenticação
A API utiliza JWT para autenticação.
""", lifespan=lifespan)

app.include_router(router=router)



if __name__ =="__main__":
    import uvicorn  as uv    
    uv.run("main:app", host="0.0.0.0", port=8000, reload=True)