from flask import Flask, request, render_template, redirect
import json
import sqlite3

app = Flask(__name__)

def criarTabela():
    conexao = sqlite3.connect("financeiro.db")
    cursor=conexao.cursor()
    cursor.execute("" \
        "CREATE TABLE IF NOT EXISTS transacoes(" 
        "id INTEGER PRIMARY KEY AUTOINCREMENT," 
        "tipo TEXT," 
        "valor REAL," 
        "descricao TEXT" 
        ")" 
    "")
    conexao.commit()
    conexao.close()

criarTabela()

@app.route("/")
def home():
    transacoes = lerTransacoesSQL()

    saldo = 0
    despesas =0
    receitas =0 
    for t in transacoes:
        if t['tipo']== "receita":
            saldo+=t['valor']
            receitas+=t['valor']
        if t['tipo']== "despesa":
            saldo-=t['valor']
            despesas+=t['valor']
    return render_template("index.html", transacoes=transacoes, saldo=saldo, receitas=receitas, despesas=despesas)
                        ##o "transações" da esquerda que conta no HTML##

@app.route("/adicionar_receita", methods=["POST"])
def adicionarReceitaSQL():
    conexao = sqlite3.connect("financeiro.db")
    cursor = conexao.cursor()

    valor = float(request.form['valor'])

    cursor.execute("INSERT INTO transacoes (tipo, valor, descricao) VALUES (?,?,?)", ("receita", valor, ""))
    conexao.commit()
    conexao.close()

    return redirect("/")


@app.route("/adicionar_despesa", methods=['POST'])
def adicionarDespesaSQL():
    conexao=sqlite3.connect("financeiro.db")
    cursor=conexao.cursor()

    valor = float(request.form['valor'])
    descricao=request.form['descricao']

    cursor.execute("INSERT INTO transacoes (tipo, valor, descricao) VALUES (?,?,?)", ("despesa", valor, descricao ))
    conexao.commit()
    conexao.close()

    return redirect("/")


@app.route("/remover", methods=['POST'])
def removerSQL():
    conexao=sqlite3.connect("financeiro.db")
    cursor=conexao.cursor()

    id_transacao = int(request.form['id'])

    cursor.execute("DELETE FROM transacoes WHERE id = ?", (id_transacao,))
    conexao.commit()
    conexao.close()
    return redirect("/")

     
def lerTransacoesSQL():
    conexao=sqlite3.connect("financeiro.db")
    conexao.row_factory = sqlite3.Row
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM transacoes")
    trans = cursor.fetchall()

    conexao.close()
    return trans    
    
    
app.run(debug=True)