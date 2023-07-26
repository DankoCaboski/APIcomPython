from connection import Connection
import mysql.connector

class EnderecoDAO:
    conexao = Connection(host="localhost", user="admin", passwd="admin123", database="ClientInformation")
    conn = conexao.get_connection()

    def insert_endereço(self, cnpj_cliente:str, logradouro:str, bairro:str, cidade:str, estado:str, pais:str):
        self.conn._open_connection()
        # Conectando ao banco de dados
        try:
            # Query SQL para inserir o valor na tabela com placeholders (%s)
            sql_insert_query = "INSERT INTO endereco (cnpj_cliente, logradouro, bairro, cidade, estado, pais) VALUES (%s, %s, %s, %s, %s, %s)"

            # Executando a query com o valor fornecido
            cursor = self.conn.cursor()
            cursor.execute(sql_insert_query, (cnpj_cliente, logradouro, bairro, cidade, estado, pais))
            self.conn.commit()

            cursor.close()
            self.conn.close()

        except mysql.connector.Error as error:
            print(f"Erro ao conectar ou inserir dados no banco de dados: {error}")

    
    def select_endereco(self, cnpj_cliente:str):
        self.conn._open_connection()
        result = []
        result.clear()
        try:
            # Query SQL para buscar os registros na tabela com filtros opcionais
            sql_select_query = "SELECT * FROM endereco WHERE cnpj_cliente = %s"
            
            cnpj_cli = [cnpj_cliente]

            cursor = self.conn.cursor()
            cursor.execute(sql_select_query, cnpj_cli)
            result = cursor.fetchall()

            cursor.close()
            self.conn.close()
                
            return result

        except mysql.connector.Error as error:
            print(f"Erro ao conectar ou buscar dados no banco de dados: {error}")


    def update_endereco(self, id, cnpj_cliente, logradouro, bairro, cidade, estado, pais):
        self.conn._open_connection()
        try:
            # Query SQL para atualizar o registro do contato
            sql_update_query = "UPDATE endereco SET cnpj_cliente = %s, logradouro = %s, bairro = %s, cidade = %s, estado = %s, pais = %s WHERE id = %s"

            # Executando a query com os valores fornecidos
            cursor = self.conn.cursor()
            cursor.execute(sql_update_query, (cnpj_cliente, logradouro, bairro, cidade, estado, pais, id))
            self.conn.commit()

            cursor.close()
            self.conn.close()

        except mysql.connector.Error as error:
            print(f"Erro ao conectar ou atualizar dados no banco de dados: {error}")


    def delete_endereco(self, id:int):
        self.conn._open_connection()
        try:
            # Query SQL para deletar o cliente pelo ID
            sql_delete_query = "DELETE FROM endereco WHERE id = %s"

            Lis_id = [id]

            # Executando a query com o valor do ID do cliente
            cursor = self.conn.cursor()
            cursor.execute(sql_delete_query, (Lis_id))
            self.conn.commit()
            
            cursor.close()
            self.conn.close()

        except mysql.connector.Error as error:
            print(f"Erro ao conectar ou deletar dados no banco de dados: {error}")