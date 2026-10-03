import sqlite3
# Conectar ao banco de dados
conexao = sqlite3.connect('usuarios.db')
cursor = conexao.cursor()

# Criar a tabela usuarios
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    email TEXT NOT NULL
)
''')
 
# Inserir um novo usuário
cursor.execute('''
INSERT INTO usuarios (nome, idade, email)
VALUES ('João', 30, 'joao@example.com')
''')
conexao.commit()
 
# Consultar usuários com idade maior que 25
cursor.execute('SELECT * FROM usuarios WHERE idade > 25')
usuarios = cursor.fetchall()
print("Usuários com idade > 25:")
for usuario in usuarios:
    print(usuario)
 
# Atualizar a idade de João
cursor.execute('''
UPDATE usuarios
SET idade = 31
WHERE nome = 'João'
''')
conexao.commit()
 
# Consultar novamente para verificar a atualização
cursor.execute('SELECT * FROM usuarios WHERE nome = "João"')
print("\nUsuário João após atualização:")
print(cursor.fetchone())
 
# Excluir o usuário João
cursor.execute('DELETE FROM usuarios WHERE nome = "João"')
conexao.commit()

# Consultar novamente para verificar a exclusão
cursor.execute('SELECT * FROM usuarios WHERE nome = "João"')
print("\nUsuário João após exclusão:")
print(cursor.fetchone())

# Fechar a conexão
conexao.close()