# repositories/base_repository.py
from backend.connection.maria_db_connection import Base, engine, SessionLocal
import sqlalchemy.orm


from backend.connection.maria_db_connection import Base

class BaseRepository:
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = SessionLocal()

    def __del__(self):
        # sécurité minimale
        self.session.close_all()