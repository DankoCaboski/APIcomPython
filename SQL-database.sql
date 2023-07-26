create database if not exists ClientInformation;

-- Configurando user e password padrão do banco de dados

CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'admin123';

GRANT SELECT, INSERT, UPDATE, DELETE ON ClientInformation.* TO 'admin'@'localhost';

FLUSH PRIVILEGES;

use ClientInformation;

create table
    cliente(
        nome VARCHAR (80) NOT NULL,
        cnpj VARCHAR(14) NOT NULL,
        status ENUM('ativo','inativo') NOT NULL DEFAULT 'ativo',
        PRIMARY KEY(cnpj)
    );
    
    create table
    endereco(
        id tinyint AUTO_INCREMENT NOT NULL,
        cnpj_cliente VARCHAR(14) NOT NULL,
        Foreign Key (cnpj_cliente) REFERENCES cliente(cnpj),
        logradouro VARCHAR (30) NOT NULL,
        bairro VARCHAR(30) NOT NULL,
		cidade VARCHAR(30) NOT NULL,
		estado VARCHAR(30) NOT NULL,
        pais VARCHAR(30) NOT NULL,
        PRIMARY KEY(id)
    );
    
    create table
    contato (
        pid int AUTO_INCREMENT NOT NULL,
		cnpj_cliente VARCHAR(14) NOT NULL,
        nome VARCHAR (80) NOT NULL,
        cargo VARCHAR(40) NOT NULL,
        telefone VARCHAR(11) NOT NULL,
        email VARCHAR(30) NOT NULL,
        Foreign Key (cnpj_cliente) REFERENCES cliente(cnpj),
        PRIMARY KEY(pid)
    );