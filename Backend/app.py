# 1 - Objetivo - Desenvolver uma API para a consulta, criaçção, ediõ e exclusão clientes de uma base de dados
# 2 - URL base - localhost
# 3 - Endpoints
    # localhost/clientes (GET)
    # localhost/clientes (POST)
    # localhost/clientes/id (GET)
    # localhost/clientes/id (PUT)
    # localhost/clientes (DELETE)

from flask import Flask, jsonify, request
from DAOS.clienteDAO import ClienteDAO
from DAOS.contatoDAO import ContatoDAO
from DAOS.enderecoDAO import EnderecoDAO


app = Flask(__name__)

"""criação dos objetos para conecxão como banco de dados"""
DAOcliente = ClienteDAO()
DAOcontato = ContatoDAO()
DAOendereco = EnderecoDAO()

"""Consultar todos os nomes"""
@app.route('/clientes',methods=['GET'])
def nomes_clientes():
    lis_clientes=[]
    for i in DAOcliente.select_clientes():
        lis_clientes.append(i[0])

    if len(lis_clientes)>=1:
        return jsonify(lis_clientes)
    else:
        # Caso a lista de nomes de clientes não seja encontrada, retorna uma resposta vazia
        return jsonify([])

"""Consultar cliente pelo CNPJ"""
@app.route('/clientes/cnpj/<int:cnpj>',methods=['GET'])   
def cons_cnpj(cnpj):
    lis_clientes=[DAOcliente.select_clientes(cnpj)]
    
    if len(lis_clientes)>=1:
        return jsonify(lis_clientes[0])
    else:
        # Caso a lista de nomes de clientes não seja encontrada, retorna uma resposta vazia
        return jsonify("não foi")
    
    """Consultar cliente pelo nome"""
@app.route('/clientes/nome/<string:nome>',methods=['GET'])   
def cons_nome(nome):
    lis_clientes=[DAOcliente.select_clientes(nome)]
    
    if len(lis_clientes)>=1:
        return jsonify(lis_clientes[0])
    else:
        # Caso a lista de nomes de clientes não seja encontrada, retorna uma resposta vazia
        return jsonify("não foi")

app.run(port=5000,host='localhost',debug=True)