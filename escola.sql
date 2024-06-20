CREATE DATABASE sistema_escolar;

USE sistema_escolar;

CREATE TABLE alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT,
    endereco VARCHAR(255)
);

CREATE TABLE funcionarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cargo VARCHAR(100)
);

CREATE TABLE notas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    aluno_id INT,
    disciplina VARCHAR(100),
    nota DECIMAL(4, 2),
    FOREIGN KEY (aluno_id) REFERENCES alunos(id)
);

CREATE TABLE informacoes_escola (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_escola VARCHAR(100) NOT NULL,
    endereco VARCHAR(255),
    telefone VARCHAR(20),
    diretor VARCHAR(100)
);

INSERT INTO alunos (nome, idade, endereco) VALUES
    ('Emanuel', 15, 'Rua A, 123'),
    ('Maria', 16, 'Rua B, 456');

INSERT INTO funcionarios (nome, cargo) VALUES
    ('Paulo', 'Professor'),
    ('Ana', 'Secretária');

INSERT INTO notas (aluno_id, disciplina, nota) VALUES
    (1, 'Matemática', 8.5),
    (1, 'Português', 7.0),
    (2, 'Matemática', 9.0),
    (2, 'Português', 8.0);

INSERT INTO informacoes_escola (nome_escola, endereco, telefone, diretor) VALUES
    ('Escola XYZ', 'Rua C, 789', '(11) 1234-5678', 'Pedro');
    
select*from informacoes_escola