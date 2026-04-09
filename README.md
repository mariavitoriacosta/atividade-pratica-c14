# 📚 Gerenciador de Biblioteca em Python

![Python](https://img.shields.io/badge/Python-3.11-blue)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-success)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

Projeto desenvolvido na disciplina de Engenharia de Software com o objetivo de aplicar conceitos de testes automatizados e CI/CD.

---

## Funcionalidades

- Cadastro de livros  
- Cadastro de usuários  
- Empréstimo e devolução de livros  
- Consulta de livros emprestados  

---

## Estrutura do projeto

```
atividade-pratica-c14/
├─ app/
├─ tests/
├─ .github/workflows/
├─ requirements.txt
├─ pyproject.toml
└─ README.md
```

---

## Testes

Os testes foram implementados com **pytest**, cobrindo:

- Fluxos normais (operações válidas)  
- Fluxos de extensão (tratamento de erros)  

---

## Pipeline

A pipeline foi configurada com **GitHub Actions** e possui:

- Execução automática dos testes  
- Geração de relatório de testes (artifact)  
- Build do projeto  

---

## Build

O projeto utiliza **build real em Python**, gerando pacotes distribuíveis com:

```bash
python -m build
```

Isso gera arquivos:

- `.whl`  
- `.tar.gz`  

💡 Em Python, o build não envolve compilação, mas sim empacotamento do projeto para distribuição.

---

## ▶️ Como executar

Instalar dependências:

```bash
pip install -r requirements.txt
```

Rodar os testes:

```bash
pytest
```

---

## Tecnologias

- Python 3.11  
- Pytest  
- GitHub Actions  
- Setuptools  

---

## Considerações finais

Este projeto foi desenvolvido com foco em boas práticas de engenharia de software, incluindo organização de código, testes automatizados e integração contínua.

A utilização de build real com `pyproject.toml` aproxima o projeto de um ambiente profissional.
