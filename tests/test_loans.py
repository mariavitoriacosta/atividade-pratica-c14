from app.services import Library
import pytest

def test_borrow_book_success():
    library = Library()
    library.add_user(1, "Ana")
    library.add_book(1, "1984", "George Orwell")

    library.borrow_book(1, 1)

    assert not library.books[1].available
    assert 1 in library.users[1].borrowed_books


def test_borrow_book_user_not_found():
    library = Library()
    library.add_book(1, "1984", "George Orwell")

    with pytest.raises(ValueError, match="Usuário não encontrado"):
        library.borrow_book(999, 1)


def test_borrow_book_not_found():
    library = Library()
    library.add_user(1, "Ana")

    with pytest.raises(ValueError, match="Livro não encontrado"):
        library.borrow_book(1, 999)


def test_borrow_book_unavailable():
    library = Library()
    library.add_user(1, "Ana")
    library.add_user(2, "João")
    library.add_book(1, "1984", "George Orwell")

    library.borrow_book(1, 1)

    with pytest.raises(ValueError, match="Livro não está disponível"):
        library.borrow_book(2, 1)