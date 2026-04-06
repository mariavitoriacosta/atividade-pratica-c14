from app.services import Library
import pytest

# testes de cenários de fluxo normal

def test_add_user_success():
    library = Library()          
    library.add_user(1, "Ana")   

    assert 1 in library.users            
    assert library.users[1].name == "Ana"

def test_add_two_users_success():
    library = Library()
    library.add_user(1, "Ana")
    library.add_user(2, "João")

    assert 1 in library.users
    assert 2 in library.users
    assert library.users[1].name == "Ana"
    assert library.users[2].name == "João"

def test_user_starts_with_no_borrowed_books():
    library = Library()
    library.add_user(1, "Ana")

    assert library.users[1].borrowed_books == []

# testes de cenários de fluxo de extensão

def test_add_user_name_empty():
    library = Library()          

    with pytest.raises(ValueError, match="Nome não pode ser vazio"):
        library.add_user(1, "")  


def test_add_user_duplicate():
    library = Library()
    library.add_user(1, "Ana")   

    with pytest.raises(ValueError, match="Usuário já cadastrado"):
        library.add_user(1, "Outro Nome")  

