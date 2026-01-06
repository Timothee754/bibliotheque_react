import sqlalchemy
from sqlalchemy.orm import declarative_base
from sql_requests.authors_request import AuthorsRequest


if __name__ == '__main__':
    instance = AuthorsRequest()
    authors = instance.get_author_by_id(1)