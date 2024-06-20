# Importa o módulo mysql.connector
import mysql.connector

# Estabelece a conexão com o banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="he182555@",
    database="sistema_escolar"
)

# Cria um objeto cursor para executar comandos SQL
cursor = db.cursor()

# Função para adicionar um aluno ao banco de dados
def adicionar_aluno(nome, idade, endereco):
    query = "INSERT INTO alunos (nome, idade, endereco) VALUES (%s, %s, %s)"
    cursor.execute(query, (nome, idade, endereco))
    db.commit()

# Função para listar os alunos do banco de dados
def listar_alunos():
    query = "SELECT * FROM alunos"
    cursor.execute(query)
    return cursor.fetchall()

# Função para adicionar um funcionário ao banco de dados
def adicionar_funcionario(nome, cargo):
    query = "INSERT INTO funcionarios (nome, cargo) VALUES (%s, %s)"
    cursor.execute(query, (nome, cargo))
    db.commit()

# Função para listar os funcionários do banco de dados
def listar_funcionarios():
    query = "SELECT * FROM funcionarios"
    cursor.execute(query)
    return cursor.fetchall()

# Função para adicionar uma nota ao banco de dados
def adicionar_nota(aluno_id, disciplina, nota):
    query = "INSERT INTO notas (aluno_id, disciplina, nota) VALUES (%s, %s, %s)"
    cursor.execute(query, (aluno_id, disciplina, nota))
    db.commit()

# Função para listar as notas de um aluno do banco de dados
def listar_notas_aluno(aluno_id):
    query = "SELECT * FROM notas WHERE aluno_id = %s"
    cursor.execute(query, (aluno_id,))
    return cursor.fetchall()

# Função para adicionar informações da escola ao banco de dados
def adicionar_informacoes_escola(nome_escola, endereco, telefone, diretor):
    query = "INSERT INTO informacoes_escola (nome_escola, endereco, telefone, diretor) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (nome_escola, endereco, telefone, diretor))
    db.commit()

# Função para obter as informações da escola do banco de dados
def obter_informacoes_escola():
    query = "SELECT * FROM informacoes_escola"
    cursor.execute(query)
    return cursor.fetchone()

# Adiciona alunos ao banco de dados
adicionar_aluno("Emanuel", 15, "Rua A, 123")
adicionar_aluno("Maria", 16, "Rua B, 456")

# Lista os alunos do banco de dados
print("Alunos:")
for aluno in listar_alunos():
    print(aluno)

# Adiciona funcionários ao banco de dados
adicionar_funcionario("Paulo", "Professor")
adicionar_funcionario("Ana", "Secretária")

# Lista os funcionários do banco de dados
print("Funcionários:")
for funcionario in listar_funcionarios():
    print(funcionario)

# Adiciona notas ao banco de dados
adicionar_nota(1, "Matemática", 8.5)
adicionar_nota(1, "Português", 7.0)
adicionar_nota(2, "Matemática", 9.0)
adicionar_nota(2, "Português", 8.0)

# Lista as notas do aluno Emanuel
print("Notas do aluno Emanuel:")
for nota in listar_notas_aluno(1):
    print(nota)

# Adiciona informações da escola ao banco de dados
adicionar_informacoes_escola(
    "Escola XYZ", "Rua C, 789", "(11) 1234-5678", "Pedro")

# Obtém as informações da escola do banco de dados
print("Informações da Escola:")
print(obter_informacoes_escola())

# Fecha a conexão com o banco de dados
db.close()
