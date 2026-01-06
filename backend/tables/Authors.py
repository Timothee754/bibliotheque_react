from backend.connection.maria_db_connection import Base, engine
import sqlalchemy

class Authors(Base):
    __tablename__ = 'authors'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.VARCHAR(100), nullable=False)
    birth_year = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)