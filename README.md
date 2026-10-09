# Controle Financeiro

Aplicação web de controle financeiro pessoal feita em Python com Flask e SQLite.

O projeto começou como um programa de terminal e foi evoluindo em etapas. Este repositório guarda cada uma delas, para mostrar o caminho percorrido, e não só o resultado final.

---

## Funcionalidades

- Adicionar receitas
- Adicionar despesas com descrição
- Ver saldo atual, total de receitas e total de despesas
- Histórico de transações
- Remover transações
- Dados guardados em banco SQLite

---

## Tecnologias

- Python
- Flask
- Jinja (templates)
- HTML
- SQLite (módulo `sqlite3`)

---

## Estrutura do repositório

```text
controle-financeiro/
├── app.py              # aplicação Flask (versão atual)
├── templates/
│   └── index.html      # página principal
├── static/             # arquivos estáticos (CSS, em breve)
├── versao_terminal/    # etapa 1: versão em terminal
├── versao_json/        # etapa 2: versão web com JSON
└── estudo_sqlite/      # script de estudo do SQLite
```

---

## Como executar

Requisitos: Python 3 e Flask.

```bash
pip install flask
python app.py
```

Depois acesse:

```text
http://127.0.0.1:5000
```

O arquivo do banco (`financeiro.db`) é criado automaticamente na primeira execução.

---

## Evolução do projeto

1. **[Versão terminal](versao_terminal/)**: programa de linha de comando, dados em JSON.
2. **[Versão web com JSON](versao_json/)**: mesma ideia em Flask, com formulários e páginas HTML.
3. **[Estudo de SQLite](estudo_sqlite/)**: testes isolados antes de usar o banco no projeto.
4. **Versão atual**: Flask com SQLite, removendo transações pelo `id`.

---

## O que pratiquei neste projeto

- Rotas e formulários (`POST`) no Flask
- Templates com Jinja (`for`, `if`, variáveis)
- Leitura e escrita de arquivos JSON
- SQL básico: `CREATE TABLE`, `INSERT`, `SELECT`, `DELETE`
- Parâmetros com `?` para evitar SQL injection
- Organização do código em funções

---

## Próximos passos

- [ ] Calcular o saldo com consultas SQL
- [ ] Estilização da página (CSS)
- [ ] Categorias de despesas
- [ ] Datas das transações
- [ ] Filtros
- [ ] Dashboard financeiro

---

## Status do projeto

🚧 Em desenvolvimento