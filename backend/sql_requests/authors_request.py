from backend.sql_requests.base_requests import BaseRepository
from backend.tables.Authors import Authors


class AuthorsRequest(BaseRepository):
    def get_all_authors(self):
        authors = self.session.query(Authors).all()
        return authors

    def get_author_by_id(self, id):
        author = self.session.query(Authors).get(id)
        return author