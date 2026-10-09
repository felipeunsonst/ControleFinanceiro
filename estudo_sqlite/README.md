# Estudo: primeiros passos com SQLite

Script de testes isolado, feito antes de usar o banco no projeto. **Não faz parte da aplicação.**

## Por que esta pasta existe

Antes de mexer no `app.py`, quis entender o SQLite num arquivo à parte, onde pudesse errar sem estragar o projeto. Mantive aqui para registrar como aprendi.

## O que o script pratica

- Conectar a um banco com `sqlite3.connect()` e usar o `cursor`
- Criar uma tabela com `CREATE TABLE IF NOT EXISTS` e uma chave primária com `AUTOINCREMENT`
- Inserir dados com `INSERT` e parâmetros (`?`)
- Gravar as alterações com `commit()`
- Consultar com `SELECT`, incluindo filtro com `WHERE`
- Apagar uma linha pelo `id` com `DELETE`

Os comandos de `INSERT` e `DELETE` estão comentados de propósito, para não criar e apagar linhas a cada execução. Para testá-los, descomente.

## Como executar

```bash
cd estudo_sqlite
python teste_sqlite.py
```

Ele cria um arquivo `financeiro.db` na pasta de onde for executado. Para visualizar as tabelas no VS Code, dá para usar a extensão **SQLite Viewer**.

## O que aprendi com os erros

- `AUTOINCREMENT` é uma palavra só.
- Em `WHERE tipo = despesa`, o SQL lê `despesa` como nome de coluna. O texto precisa ir como parâmetro (`?`) ou entre aspas simples.
- Uma tupla com um único valor precisa da vírgula: `("despesa",)`.
- Sem `commit()`, as alterações não são gravadas.
- `CREATE TABLE IF NOT EXISTS` não altera uma tabela que já existe: se a estrutura mudar, é preciso recriar o banco.