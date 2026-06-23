CREATE DATABASE estoque;

USE estoque;

CREATE TABLE produtos (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
	quantidade int(10)
);

select * from produtos;