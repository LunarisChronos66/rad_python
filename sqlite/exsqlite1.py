import sqlite3

# Conectar ao banco de dados
conector = sqlite3.connect("estacio.db")
cursor = conector.cursor()

# Criar a tabela cadastro
comando_sql = "CREATE TABLE IF NOT EXISTS cadastro(codigo inteiro, nome text, idade integer)"
cursor.execute(comando_sql)

# Inserir dados na tabela
comando_sql = "INSERT INTO cadastro (codigo, nome, idade) VALUES (1309, 'Tonico', 3)"
cursor.execute(comando_sql)

# Confirmar as operações
conector.commit()

# Fechar a conexão
cursor.close()
conector.close()