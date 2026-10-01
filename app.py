from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
    with open('dados.json', "r", encoding='utf-8') as arquivo:
        transacoes = json.load(arquivo)

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

    

app.run(debug=True)