import sqlite3
import matplotlib.pyplot as plt

# Conectar ao banco de dados SQLite (ou criar um novo banco de dados)
conn = sqlite3.connect('academia.db')
cursor = conn.cursor()

# Criar tabela para armazenar as informações dos usuários
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cadastro (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        altura REAL NOT NULL,
        peso1 REAL NOT NULL,
        peso2 REAL NOT NULL,
        peso3 REAL NOT NULL
    )
''')

# Função para calcular o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Função para criar um novo registro e exibir resultados imediatamente
def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    altura = float(input("Digite a altura do usuário (em metros): "))
    pesos = []

    for i in range(1, 4):
        peso = float(input(f"Digite o peso {i} (em kg): "))
        pesos.append(peso)
        # Inserir no banco de dados
    
    cursor.execute('''
        INSERT INTO cadastro (nome, altura, peso1, peso2, peso3)
        VALUES (?, ?, ?, ?, ?)
        ''', (nome, altura, pesos[0], pesos[1], pesos[2])) 
    conn.commit()

    # Calcular IMCs e mostrar resultados
    imcs = [calcular_imc(p, altura) for p in pesos]

    for i, imc in enumerate(imcs, 1):
        print(f'Peso {i}: {pesos[i-1]} kg, IMC {i}: {imc:.2f}')

    # Plotar gráfico
    plt.plot(['Medição 1', 'Medição 2', 'Medição 3'], imcs, marker='o')
    plt.title(f'Evolução do IMC de {nome}')
    plt.xlabel('Medições')
    plt.ylabel('IMC')
    plt.ylim(0, 40)
    plt.grid(True)
    plt.show()

# Exemplo de uso
criar_usuario()
# Fechar a conexão com o banco de dados
conn.close()

