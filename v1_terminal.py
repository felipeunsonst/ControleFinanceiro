import json

with open('dados.json', "r", encoding='utf-8') as arquivo:
    transacoes = json.load(arquivo)

print ("Bem vindo ao controle financeiro\n")
nome = input("Digite seu nome:\n")
print(f"Ola, {nome}, o que você deseja?\n")

saldo = 0
for t in transacoes:
     if t['tipo']== "receita":
          saldo+=t['valor']
     if t['tipo']== "despesa":
          saldo-=t['valor']

def Receita():
    global saldo
    while True:
        try:
            print("Digite o valor a ser adicionado")
            valor =float(input())
            transacoes.append({
                "tipo": "receita",
                "valor": valor,
                "descricao": ""
            })
            saldo += valor
            print("Valor adicionado com sucesso\n")
            break
        except ValueError:
            print("Valor inválido. Por favor, digite um número.\n")

def Despesa():
    global saldo
    while True:
        try:
            print("Digite a despesa\n")
            valor=float(input())
            print("Qual o motivo do gasto?\n")
            motivo=input()
            transacoes.append({
                "tipo": "despesa",
                "valor": valor,
                "descricao": motivo
            })
            saldo -=valor
            print("Valor descontado")
            break
        except ValueError:
            print("Valor inválido. Por favor, digite um número.\n")

def Saldo():
    print(f"saldo: {saldo}\n")

def Historico():
    for i, t in enumerate(transacoes, start=1):
        if t['tipo'] == "receita":
            print(f"{i}. receita  | +R${t['valor']:.2f}")
        elif t['tipo'] == "despesa":
            print(f"{i}. despesa | -R${t['valor']:.2f} | motivo: {t['descricao']}")
    print()

def Resumo():
    contReceita=0
    contDespesas=0
    totalReceita=0
    totalDespesas=0
    for t in transacoes:
        if t['tipo']=='receita':
            contReceita+=1
            totalReceita+=t['valor']
        if t['tipo']=='despesa':
            contDespesas+=1
            totalDespesas+=t['valor']
    print(f"Total de receita: {contReceita}, com valor acumulado de: {totalReceita}")
    print(f"Total de despesa: {contDespesas}, com valor acumulado de: -{totalDespesas}")
    print(f"Saldo final: {saldo}\n")

def Remover():
    while True:
        try:
            print("Digite o valor e o motivo da despesa que deseja remover")
            v=float(input("Valor:"))
            m=input("Motivo:")
            encontrado = False
            for t in transacoes:
                if t['tipo']=='despesa' and t['valor']==v and t['descricao']==m:
                    global saldo
                    saldo+=t['valor']
                    transacoes.remove(t)
                    print("Despesa removida com sucesso\n")
                    encontrado = True
                    break
            
            if not encontrado:
                print("Despesa não encontrada.\n")
            break
        except ValueError:
            print("Valor inválido. Por favor, digite um número.\n")

while True:
    print("1-Adicionar receita")
    print("2-Adicionar despesa")
    print("3-Ver saldo")
    print("4-Ver transações")
    print("5-Resumo")
    print("6-Remover Despesas")
    print("0-Sair\n")

    opcao = input()
    if opcao == "1": #adicionar receita
       Receita()
    elif opcao == "2": #adicionar despesa
        Despesa()
    elif opcao == "3": #saldo
        Saldo()
    elif opcao == "4": #ver historico
        Historico()
    elif opcao == "5": #resumo
       Resumo()
    elif opcao =="6": #remover despesa
        Remover()
    elif opcao == "0":
        break
    else:
        print("Opção invalida")

with open('dados.json', "w", encoding='utf-8') as arquivo:
            json.dump(transacoes, arquivo, ensure_ascii=False, indent=4)
        
