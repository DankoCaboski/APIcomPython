from connection import Connection
import mysql.connector

class ClienteDAO:
    conexao = Connection(host="localhost", user="admin", passwd="admin123", database="ClientInformation")
    conn = conexao.get_connection()

    def insert_cliente(self, nome:str, cnpj:int):
        self.conn._open_connection()
        # Conectando ao banco de dados
        try:
            # Query SQL para inserir o valor na tabela com placeholders (%s)
            sql_insert_query = "INSERT INTO cliente (nome, cnpj) VALUES (%s, %s)"

            # Executando a query com o valor fornecido
            cursor = self.conn.cursor()
            cursor.execute(sql_insert_query, (nome, str(cnpj)))  # Usando os placeholders com os valores fornecidos
            self.conn.commit()

            print("Valor inserido com sucesso!")

        except mysql.connector.Error as error:
            print(f"Erro ao conectar ou inserir dados no banco de dados: {error}")

        finally:
            # Fechando a conexão
            if self.conn.is_connected():
                cursor.close()
                self.conn.close()
                print("Conexão ao banco de dados fechada.")

    
    def select_clientes(self, nome=None, cnpj:int=None):
        self.conn._open_connection()
        result = []
        result.clear()
        try:
            # Query SQL para buscar os registros na tabela com filtros opcionais
            sql_select_query = "SELECT * FROM cliente"

            # lista que recebe os clientes
            cliente = [nome]
            cnpj_cli = str(cnpj)

            if nome is None and cnpj is None:
                cursor = self.conn.cursor()
                cursor.execute(sql_select_query,)
                result = cursor.fetchall()

            
            elif nome is not None:
                try:
                    int(nome)
                    sql_select_query += " WHERE cnpj = %s"
                    cursor = self.conn.cursor()
                    cursor.execute(sql_select_query, (cliente))
                    result = cursor.fetchall()
                except:
                    if cnpj is not None:
                        sql_select_query += " WHERE nome = %s AND cnpj = %s"
                        cursor = self.conn.cursor()
                        cursor.execute(sql_select_query, (cliente, cnpj_cli))
                        result = cursor.fetchall()
                    else:
                        sql_select_query += " WHERE nome = %s"
                        cursor = self.conn.cursor()
                        cursor.execute(sql_select_query, (cliente))
                        result = cursor.fetchall()

                cursor.close()
                self.conn.close()
                
            return result

        except mysql.connector.Error as error:
            print(f"Erro ao conectar ou buscar dados no banco de dados: {error}")


    def update_status_cliente(self, cnpj:int, novo_status:str):
        self.conn._open_connection()
        try:
            # Query SQL para atualizar o status do cliente
            sql_update_query = "UPDATE cliente SET status = %s WHERE cnpj = %s"

            # Executando a query com os valores fornecidos
            cursor = self.conn.cursor()
            cursor.execute(sql_update_query, (novo_status, cnpj))
            self.conn.commit()

            cursor.close()
            self.conn.close()

        except mysql.connector.Error as error:
            print(f"Erro ao conectar ou atualizar dados no banco de dados: {error}")

    def delete_cliente(self, cnpj:int):
        self.conn._open_connection()
        try:
            # Query SQL para deletar o cliente pelo ID
            sql_delete_query = "DELETE FROM cliente WHERE cnpj = %s"

            # Executando a query com o valor do ID do cliente
            cursor = self.conn.cursor()
            cursor.execute(sql_delete_query, (cnpj,))
            self.conn.commit()

            print("Cliente deletado com sucesso!")

        except mysql.connector.Error as error:
            print(f"Erro ao conectar ou deletar dados no banco de dados: {error}")

        finally:
            # Fechando a conexão
            if self.conn.is_connected():
                cursor.close()
                self.conn.close()
                print("Conexão ao banco de dados fechada.")