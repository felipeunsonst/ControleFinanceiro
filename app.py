from flask import Flask, request, render_template, redirect
import json

app = Flask(__name__)

@app.route("/")
def home():
    transacoes=lerTransacoes()

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
def adicionarReceita():
    transacoes=lerTransacoes()

    valor = float(request.form['valor'])
    transacoes.append({
        "tipo": "receita",
        "valor": valor,
        "descricao": ""
    })

    salvarTransacoes(transacoes)
    
    return redirect("/")

@app.route("/adicionar_despesa", methods=['POST'])
def adicionarDespesa():
    transacoes=lerTransacoes()

    valor= float(request.form['valor'])
    descricao = request.form['descricao']
    transacoes.append({
        "tipo" : "despesa",
        "valor" : valor,
        "descricao" : descricao
    })

    salvarTransacoes(transacoes)

    return redirect("/")

@app.route("/remover", methods=['POST'])
def remover():
    transacoes=lerTransacoes()

    posicao = int(request.form['posicao'])
    del transacoes[posicao]

    salvarTransacoes(transacoes)
    return redirect("/")
     
def lerTransacoes():
    with open('dados.json', 'r', encoding='utf-8') as arquivo:
        transacoes = json.load(arquivo)

    return transacoes

def salvarTransacoes(transacoes):
    with open('dados.json', 'w', encoding='utf-8') as arquivo:
        json.dump(transacoes, arquivo, ensure_ascii=False, indent=4)
    
    
    
app.run(debug=True)