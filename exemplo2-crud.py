import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('estacio dados.db')
cursor = conexao.cursor()

# Criar a tabela alunos_estacio
cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos_estacio (
    matricula INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    sexo TEXT NOT NULL
)
''')

# Inserir 6 alunos
cursor.executemany('''
INSERT INTO alunos_estacio (matricula, nome, sobrenome, idade, sexo)
VALUES (?, ?, ?, ?, ?)
''', [
    (1, 'Gabriel', 'Barbosa', 22, 'M'),
    (2, 'João', 'Silva', 24, 'M'),
    (3, 'Maria', 'Santos', 26, 'F'),
    (4, 'Lucas', 'Oliveira', 23, 'M'),
    (5, 'Ana', 'Souza', 27, 'F'),
    (6, 'Pedro', 'Costa', 25, 'M')
])

conexao.commit()

# Consultar alunos com idade abaixo de 25 anos
cursor.execute('SELECT * FROM alunos_estacio WHERE idade < 25')
alunos = cursor.fetchall()

print("Alunos com idade abaixo de 25 anos:")
for aluno in alunos:
    print(aluno)

# Consultar alunos com idade acima de 25 anos
cursor.execute('SELECT * FROM alunos_estacio WHERE idade > 25')
alunos = cursor.fetchall()

print("\nAlunos com idade acima de 25 anos:")
for aluno in alunos:
    print(aluno)

# Atualizar o sobrenome e a idade de Gabriel
cursor.execute('''
UPDATE alunos_estacio
SET sobrenome = 'Barros Barbosa', idade = 23
WHERE nome = 'Gabriel'
''')

conexao.commit()

# Consultar Gabriel após atualização
cursor.execute('SELECT * FROM alunos_estacio WHERE nome = "Gabriel"')

print("\nGabriel após atualização:")
print(cursor.fetchone())

# Excluir os dados de Gabriel e de mais um colega
cursor.execute('DELETE FROM alunos_estacio WHERE nome = "Gabriel"')
cursor.execute('DELETE FROM alunos_estacio WHERE nome = "João"')

conexao.commit()

# Consultar novamente para verificar a exclusão
cursor.execute('SELECT * FROM alunos_estacio WHERE nome = "Gabriel"')

print("\nGabriel após exclusão:")
print(cursor.fetchone())

cursor.execute('SELECT * FROM alunos_estacio WHERE nome = "João"')

print("\nJoão após exclusão:")
print(cursor.fetchone())()

# Fechar a conexão
conexao.close()