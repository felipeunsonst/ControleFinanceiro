import sqlite3

conexao = sqlite3.connect("financeiro.db") ##abre a conexão com o arquivo
cursor = conexao.cursor()## mensageiro que leva os comandos SQL ate o banco

cursor.execute("" 
    "CREATE TABLE IF NOT EXISTS transacoes(" 
        "id INTEGER PRIMARY KEY AUTOINCREMENT," 
        "tipo TEXT," 
        "valor REAL," 
        "descricao TEXT" 
        ")" 
"")


##cursor.execute("INSERT INTO transacoes (tipo, valor, descricao) VALUES (?,?,?)", ("receita", 1500, "" ))
##cursor.execute("INSERT INTO transacoes (tipo, valor, descricao) VALUES (?,?,?)", ("despesa", 350, "mercado" ))
##cursor.execute("DELETE FROM transacoes WHERE id = 2")
conexao.commit()

cursor.execute("SELECT * FROM transacoes WHERE tipo = ?",  ("despesa",))
print(cursor.fetchall())

conexao.close()