import sqlalchemy

class DatabaseEngine:
    def __init__(self):
        self._engine = sqlalchemy.create_engine(
            "mariadb+mariadbconnector://production:123456+Aze@172.16.35.114:3306/bibliotheque"
        )

    def get_engine(self):
        return self._engine
