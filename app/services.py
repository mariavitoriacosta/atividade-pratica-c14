from app.models import Book, User


class Library:
    def __init__(self):
        self.books = {}
        self.users = {}

    # Livros

    def add_book(self, book_id, title, author):
        if not title.strip():
            raise ValueError("Título não pode ser vazio")
        if not author.strip():
            raise ValueError("Autor não pode ser vazio")
        if book_id in self.books:
            raise ValueError("Livro já cadastrado")
        self.books[book_id] = Book(book_id, title, author)

    def remove_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Livro não encontrado")
        if not self.books[book_id].available:
            raise ValueError("Livro está emprestado e não pode ser removido")
        del self.books[book_id]

    # Usuários

    def add_user(self, user_id, name):
        if not name.strip():
            raise ValueError("Nome não pode ser vazio")
        if user_id in self.users:
            raise ValueError("Usuário já cadastrado")
        self.users[user_id] = User(user_id, name)

    # Empréstimos

    def borrow_book(self, user_id, book_id):
        if user_id not in self.users:
            raise ValueError("Usuário não encontrado")
        if book_id not in self.books:
            raise ValueError("Livro não encontrado")
        if not self.books[book_id].available:
            raise ValueError("Livro não está disponível")
        self.books[book_id].available = False
        self.users[user_id].borrowed_books.append(book_id)

    def return_book(self, user_id, book_id):
        if user_id not in self.users:
            raise ValueError("Usuário não encontrado")
        if book_id not in self.users[user_id].borrowed_books:
            raise ValueError("Este livro não foi emprestado por este usuário")
        self.books[book_id].available = True
        self.users[user_id].borrowed_books.remove(book_id)

    def get_borrowed_books(self, user_id):
        if user_id not in self.users:
            raise ValueError("Usuário não encontrado")
        return [
            self.books[book_id]
            for book_id in self.users[user_id].borrowed_books
        ]