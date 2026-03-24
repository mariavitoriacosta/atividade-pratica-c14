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
