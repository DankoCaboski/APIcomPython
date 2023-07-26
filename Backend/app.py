# 1 - Objetivo - Desenvolver uma API para a consulta, criaçção, ediõ e exclusão clientes de uma base de dados
# 2 - URL base - localhost
# 3 - Endpoints
    # localhost/clientes (GET)
    # localhost/clientes (POST)
    # localhost/clientes/id (GET)
    # localhost/clientes/id (PUT)
    # localhost/clientes (DELETE)

from DAOS.clienteDAO import ClienteDAO
from DAOS.contatoDAO import ContatoDAO
from DAOS.enderecoDAO import EnderecoDAO

end =  EnderecoDAO()
end.delete_endereco(1)
print(end.select_endereco(8))

#cliDAO = ClienteDAO()
#cliDAO.insert_cliente("paulo", 8)

#clientDAO = ContatoDAO()
#clientDAO.insert_contato(8,"rogerio", "gestor", 888, "aal")
#print("oi")
#print(clientDAO.select_contato(8))

#clientDAO.delete_cliente(2)