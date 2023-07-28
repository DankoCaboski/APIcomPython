from DAOS.clienteDAO import ClienteDAO
from DAOS.contatoDAO import ContatoDAO
from DAOS.enderecoDAO import EnderecoDAO

"""criação dos objetos para conecxão como banco de dados"""
DAOcliente = ClienteDAO()
DAOcontato = ContatoDAO()
DAOendereco = EnderecoDAO()
DAOcliente.delete_cliente(2)
