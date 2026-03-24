from app.models import Book


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        if not title.strip():
            raise ValueError("Título não pode ser vazio")

        if book_id in self.books:
            raise ValueError("Livro já cadastrado")

        self.books[book_id] = Book(book_id, title, author)