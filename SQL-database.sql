create database if not exists ClientInformation;

-- Configurando user e password padrão do banco de dados

CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'admin123';

GRANT SELECT, INSERT, UPDATE, DELETE ON ClientInformation.* TO 'admin'@'localhost';

FLUSH PRIVILEGES;

use ClientInformation;

DROP TABLE IF exists cliente;

create table
    cliente(
        nome VARCHAR (80) NOT NULL,
        cnpj VARCHAR(14) NOT NULL,
        status ENUM('ativo','inativo') NOT NULL DEFAULT 'ativo',
        PRIMARY KEY(cnpj)
    );
    
INSERT INTO cliente (nome, cnpj)
	VALUES
	  ('Ana', 1),
	  ('José', 2),
	  ('Paulo', 3),
      ('Debora', 4),
	  ('Janaina', 5),
	  ('Paula', 6);
    
DROP TABLE IF exists endereco;    
    
    create table
    endereco(
        id tinyint AUTO_INCREMENT NOT NULL,
        cnpj_cliente VARCHAR(14) NOT NULL,
        logradouro VARCHAR (30) NOT NULL,
        bairro VARCHAR(30) NOT NULL,
		cidade VARCHAR(30) NOT NULL,
		estado VARCHAR(30) NOT NULL,
        pais VARCHAR(30) NOT NULL,
        PRIMARY KEY(id),
        Foreign Key (cnpj_cliente) REFERENCES cliente(cnpj) ON DELETE CASCADE
    );
    
INSERT INTO endereco (id, cnpj_cliente, logradouro, bairro, cidade, estado, pais)
	VALUES
		(1,1, 'Casa', 'Residencial Gazo', 'SJC', 'SP', 'BR'),
        (2,1, 'Apartamento', 'Residencial Itauan', 'Sorocaba', 'SC', 'BR'),
        (3,2, 'Casa', 'Residencial Gazo', 'SJC', 'SP', 'BR'),
        (4,3, 'Apartamento', 'Residencial Itauan', 'Sorocaba', 'SC', 'BR');
    
DROP TABLE IF exists contato;   
    
    create table
    contato (
        pid int AUTO_INCREMENT NOT NULL,
		cnpj_cliente VARCHAR(14) NOT NULL,
        nome VARCHAR (80) NOT NULL,
        cargo VARCHAR(40) NOT NULL,
        telefone VARCHAR(11) NOT NULL,
        email VARCHAR(30) NOT NULL,
        Foreign Key (cnpj_cliente) REFERENCES cliente(cnpj) ON DELETE CASCADE,
        PRIMARY KEY(pid)
    );