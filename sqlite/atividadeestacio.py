import sqlite3

# Conectar ao banco de dados
conector = sqlite3.connect("estacio.db")
cursor = conector.cursor()

# Inserir dados na tabela
comando_sql = "INSERT INTO cadastro (codigo, nome, idade) VALUES (1379, 'Aueue', 5)"
cursor.execute(comando_sql)

comando_sql = "INSERT INTO cadastro (codigo, nome, idade) VALUES (1340, 'Fernando', 9)"
cursor.execute(comando_sql)

# Confirmar as operações
conector.commit()

# Fechar a conexão
cursor.close()
conector.close()