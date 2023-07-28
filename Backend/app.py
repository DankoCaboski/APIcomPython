# 1 - Objetivo - Desenvolver uma API para a consulta, criaçção, ediõ e exclusão clientes de uma base de dados
# 2 - URL base - localhost
# 3 - Endpoints
    # localhost/clientes - retornalista de clientes
    # localhost/clientes/cnpj/ - retorna o nome do clinete em função de seu CNPJ, preencher o CNPJ desejado apos a ultima '/'
    # localhost/clientes/nome/ - retorna o nome do clinete em função de seu nome, preencher o nome desejado apos a ultima '/'
    # localhost/clientes/id (PUT)
    # localhost/clientes (DELETE)

from flask import Flask, jsonify, request
from flask_cors import CORS
from DAOS.clienteDAO import ClienteDAO
from DAOS.contatoDAO import ContatoDAO
from DAOS.enderecoDAO import EnderecoDAO


app = Flask(__name__)
CORS(app)

"""criação dos objetos para conecxão como banco de dados"""
DAOcliente = ClienteDAO()
DAOcontato = ContatoDAO()
DAOendereco = EnderecoDAO()

"""Consultar todos os nomes"""
@app.route('/clientes',methods=['GET'])
def nomes_clientes():
    lis_clientes=[]
    for i in DAOcliente.select_clientes():
        lis_clientes.append(i)

    if len(lis_clientes)>=1:
        return jsonify(lis_clientes)
    else:
        return jsonify([])

"""Consultar cliente pelo CNPJ"""
@app.route('/clientes/<int:cnpj>',methods=['GET'])   
def cons_cnpj(cnpj):
    lis_clientes=[DAOcliente.select_clientes(cnpj)]
    
    if len(lis_clientes)>=1:
        return jsonify(lis_clientes[0])
    else:
        return jsonify("não foi")
    
    """Consultar cliente pelo nome"""
@app.route('/clientes/<string:nome>',methods=['GET'])   
def cons_nome(nome):
    lis_clientes=[DAOcliente.select_clientes(nome)]
    
    if len(lis_clientes)>=1:
        return jsonify(lis_clientes[0])
    else:
        return jsonify("não foi")
    
@app.route('/clientes/flipStatus/<int:cnpj>',methods=['PUT'])   
def flip_status(cnpj):
    status =  DAOcliente.select_clientes(cnpj)
    if status[0][2] == "ativo":
        DAOcliente.update_status_cliente(cnpj, "inativo")
    else:
        DAOcliente.update_status_cliente(cnpj, "ativo")
    return '', 200

@app.route('/clientes/delete/<int:cnpj>',methods=['DELETE'])   
def delete(cnpj):
    DAOcliente.delete_cliente(cnpj)
    return '', 200


app.run(port=5000,host='localhost',debug=True)