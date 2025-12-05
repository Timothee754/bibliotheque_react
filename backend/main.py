import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://production:123456+Aze@172.16.35.114:3306/bibliotheque")

Base = declarative_base()
class authors(Base):
    __tablename__ = 'authors'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.VARCHAR(255), nullable=False)
    birth_year = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

employees = session.query(authors).all()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for author in employees:
        print(f"ID: {author.id}, Name: {author.name}, Birth Year: {author.birth_year}")