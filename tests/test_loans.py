from app.services import Library
import pytest

# testes de cenários de fluxo normal

def test_borrow_book_success():
    library = Library()
    library.add_user(1, "Ana")
    library.add_book(1, "1984", "George Orwell")

    library.borrow_book(1, 1)

    assert not library.books[1].available
    assert 1 in library.users[1].borrowed_books

def test_return_book_success():
    library = Library()
    library.add_user(1, "Ana")
    library.add_book(1, "1984", "George Orwell")
    library.borrow_book(1, 1)

    library.return_book(1, 1)

    assert library.books[1].available is True
    assert 1 not in library.users[1].borrowed_books

def test_get_borrowed_books_success():
    library = Library()
    library.add_user(1, "Ana")
    library.add_book(1, "1984", "George Orwell")
    library.borrow_book(1, 1)

    borrowed_books = library.get_borrowed_books(1)

    assert len(borrowed_books) == 1
    assert borrowed_books[0].title == "1984"
    assert borrowed_books[0].author == "George Orwell"

def test_get_borrowed_books_empty_list():
    library = Library()
    library.add_user(1, "Ana")

    borrowed_books = library.get_borrowed_books(1)

    assert borrowed_books == []

def test_user_can_borrow_two_different_books():
    library = Library()
    library.add_user(1, "Ana")
    library.add_book(1, "1984", "George Orwell")
    library.add_book(2, "Dom Casmurro", "Machado de Assis")

    library.borrow_book(1, 1)
    library.borrow_book(1, 2)

    assert 1 in library.users[1].borrowed_books
    assert 2 in library.users[1].borrowed_books
    assert library.books[1].available is False
    assert library.books[2].available is False

# testes de cenários de fluxo de extensão

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