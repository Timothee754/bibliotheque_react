import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

engine = sqlalchemy.create_engine(
    "mariadb+mariadbconnector://production:123456+Aze@172.16.35.114:3306/bibliotheque"
)
SessionLocal = sessionmaker(bind=engine)
