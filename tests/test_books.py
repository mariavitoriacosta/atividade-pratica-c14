from app.services import Library
import pytest


def test_add_book_success():
    library = Library()
    library.add_book(1, "1984", "George Orwell")

    assert 1 in library.books
    assert library.books[1].title == "1984"


def test_add_book_title_empty():
    library = Library()

    with pytest.raises(ValueError, match="Título não pode ser vazio"):
        library.add_book(1, "", "Autor")

def test_add_book_author_empty():
    library = Library()

    with pytest.raises(ValueError, match="Autor não pode ser vazio"):
        library.add_book(1, "1984", "")


def test_add_book_duplicate():
    library = Library()
    library.add_book(1, "1984", "George Orwell")

    with pytest.raises(ValueError, match="Livro já cadastrado"):
        library.add_book(1, "Outro Livro", "Outro Autor")


def test_remove_book_success():
    library = Library()
    library.add_book(1, "1984", "George Orwell")

    library.remove_book(1)

    assert 1 not in library.books


def test_remove_book_not_found():
    library = Library()

    with pytest.raises(ValueError, match="Livro não encontrado"):
        library.remove_book(999)


def test_remove_book_borrowed():
    library = Library()
    library.add_book(1, "1984", "George Orwell")
    library.add_user(1, "Marcelo")
    library.borrow_book(1, 1)

    with pytest.raises(ValueError, match="Livro está emprestado e não pode ser removido"):
        library.remove_book(1)