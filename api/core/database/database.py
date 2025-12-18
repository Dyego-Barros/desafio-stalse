from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


Base = declarative_base()

engine = create_engine("sqlite:///desafio.db", connect_args={"check_same_thread": False,"autocommit":False})

SessionLocal =  sessionmaker(bind=engine, autoflush=False)


class Database:
    
    def connection(self):
        """Retorna Session de conexão com banco de dadoss"""
        try:
            db = SessionLocal()
            yield db
        finally:
            db.close()