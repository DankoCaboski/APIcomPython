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
        (2,2, 'Apartamento', 'Residencial Itauan', 'Sorocaba', 'SC', 'BR'),
        (3,3, 'Casa', 'Residencial Gazo', 'SJC', 'SP', 'BR'),
        (4,4, 'Apartamento', 'Residencial Itauan', 'Sorocaba', 'SC', 'BR'),
        (5,4, 'Casa', 'Residencial Itauan', 'Taubate', 'SP', 'BR'),
        (6,4, 'Casa', 'Residencial Itauan', 'Taubate', 'SP', 'BR'),
        (7,4, 'Apartamento', 'Residencial Itauan', 'Sorocaba', 'SC', 'BR');
    
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
    
INSERT INTO contato (pid, cnpj_cliente, nome, cargo, telefone, email)
	VALUES
		(1, 2, 'Jeremy', 'Gestor', 68995646129, 'asd@asd'),
		(2, 2, 'Natália', 'Colaborador', 27999785222, 'avdssd@asd'),
 		(3, 2, 'Rafaela', 'Colaborador', 86979584621, 'sebsdv@asd'),
        (4, 2, 'Lívia', 'Diretor', 12975249139, 'ssdvsv@asd'),
        (5, 3, 'Charles', 'Gestor', 68995646129, 'sdvv@asd'),
		(6, 3, 'George', 'Colaborador', 27999785112, 'ssfh@asd'),
 		(7, 4, 'Amy', 'Colaborador', 86979589221, 'safn@asd'),
        (8, 4, 'Jose', 'Colaborador', 12975249139, 'cnft@asd'),
		(9, 4, 'Elizabeth', 'Diretor', 12975249139, 'asgrd@asd'),
        (10, 4, 'Charles', 'Gestor', 68995646124, 'sbkd@asd'),
		(11, 5, 'George', 'Colaborador', 27999788342, 'edab@asd'),
 		(12, 5, 'Amy', 'Colaborador', 86979589235, 'sbwr@asd'),
        (13, 5, 'Sylvia', 'Diretor', 12975249689, 'atnsd@asd'),
		(14, 5, 'Lívia', 'Colaborador', 12977249139, 'yydg@asd'),
        (15, 5, 'George', 'Gestor', 27999785142, 'xfts@asd'),
 		(16, 5, 'Amy', 'Colaborador', 86979853221, 'hrdt@asd'),
        (17, 6, 'Amber', 'Colaborador', 12297529139, 'wtfr@asd'),
		(18, 6, 'Lawrence', 'Colaborador', 12975249139, '5hyu@asd'),
        (19, 6, 'George', 'Colaborador', 27999787122, 'vbwn@asd'),
 		(20, 6, 'Amy', 'Colaborador', 86979585921, 'fgth@asd'),
        (21, 6, 'Catherine', 'Diretor', 12975299989, 'wher@asd'),
		(22, 6, 'Lívia', 'Gestor', 12769249139, 'asad@asd')