# 📚 Gerenciador de Biblioteca em Python

![Python](https://img.shields.io/badge/Python-3.11-blue)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-success)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

Projeto desenvolvido na disciplina de Engenharia de Software com o objetivo de aplicar conceitos de testes automatizados, build e CI/CD.

---

## Funcionalidades

- Cadastro de livros  
- Cadastro de usuários  
- Empréstimo e devolução de livros  
- Consulta de livros emprestados  

---

## Estrutura do projeto

```text
atividade-pratica-c14/
├─ app/
├─ tests/
├─ scripts/
│  └─ notify.py
├─ dist/
├─ .github/
│  └─ workflows/
│     └─ ci.yml
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

A pipeline foi configurada com **GitHub Actions** e possui as seguintes etapas:

- **test**: executa os testes automatizados do projeto  
- **build**: gera os pacotes distribuíveis da aplicação  
- **deploy**: simula a etapa de deploy após o build  
- **notify**: envia uma notificação por e-mail com o resultado da pipeline  

O fluxo da pipeline segue a ordem:

**test → build → deploy → notify**

Além disso, a pipeline inclui:

- Execução automática a cada push e pull request  
- Geração de artifact com relatório de testes  
- Empacotamento do projeto para distribuição  

---

## Build

O projeto utiliza **build real em Python**, gerando pacotes distribuíveis com:

```bash
python -m build
```

Esse comando gera arquivos como:

- `.whl`  
- `.tar.gz`  

Em Python, o build não representa compilação como em linguagens compiladas, mas sim o empacotamento da aplicação para distribuição.

---

## Como executar

Instale as dependências com:

```bash
pip install -r requirements.txt
```

Execute os testes com:

```bash
pytest
```

Para gerar o build do projeto:

```bash
python -m build
```

---

## Tecnologias

- Python 3.11  
- Pytest  
- GitHub Actions

---

## Considerações finais

Este projeto foi desenvolvido com foco em boas práticas de engenharia de software, incluindo organização de código, testes automatizados, integração contínua e automação de etapas do processo de entrega.

A utilização de `pyproject.toml` para build e a presença das etapas de **deploy** e **notify** aproximam o projeto de um cenário mais próximo do ambiente profissional.
