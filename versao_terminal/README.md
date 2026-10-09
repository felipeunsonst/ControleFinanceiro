# Versão 1: Terminal

Primeira etapa do projeto: um controle financeiro em linha de comando.

## Por que esta pasta existe

Foi a base de tudo. Aqui treinei funções, tratamento de erros com `try/except`, laços de repetição e leitura e escrita de arquivos JSON. Ela fica no repositório para registrar o ponto de partida.

## Funcionalidades

Um menu com as opções:

1. Adicionar receita
2. Adicionar despesa
3. Ver saldo
4. Ver transações
5. Resumo
6. Remover despesas
0. Sair

## Como executar

```bash
cd versao_terminal
python v1_terminal.py
```

O programa lê o arquivo `dados.json` da pasta onde é executado. Ele precisa existir: pode ser uma lista vazia (`[]`).

Cada transação tem este formato:

```json
{ "tipo": "despesa", "valor": 30.0, "descricao": "lanche" }
```

## Limitações conhecidas

Foram o que motivou as etapas seguintes:

- O saldo é guardado em uma variável separada, em vez de calculado a partir das transações.
- Os dados só são salvos ao sair pela opção `0`. Se o programa fechar de outro jeito, as alterações da sessão se perdem.
- A remoção é feita digitando valor e motivo, e só remove a primeira transação que bater.
- Não tem interface gráfica.

## Próxima etapa

[Versão web com Flask e JSON](../versao_json/)