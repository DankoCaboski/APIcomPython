from connection import Connection
import mysql.connector

class ContatoDAO:
    conexao = Connection(host="localhost", user="admin", passwd="admin123", database="ClientInformation")
    conn = conexao.get_connection()

    def insert_contato(self, cnpj_cnpj_cliente:str, nome:str, cargo:str, telefone, email):
        self.conn._open_connection()
        # Conectando ao banco de dados
        try:
            # Query SQL para inserir o valor na tabela com placeholders (%s)
            sql_insert_query = "INSERT INTO contato (cnpj_cliente, nome, cargo, telefone, email) VALUES (%s, %s, %s, %s, %s)"

            # Executando a query com o valor fornecido
            cursor = self.conn.cursor()
            cursor.execute(sql_insert_query, (cnpj_cnpj_cliente, nome, cargo, str(telefone), email))  # Usando os placeholders com os valores fornecidos
            self.conn.commit()

        except mysql.connector.Error as error:
            print(f"Erro ao conectar ou inserir dados no banco de dados: {error}")

        finally:
            # Fechando a conexão
            if self.conn.is_connected():
                cursor.close()
                self.conn.close()
                print("Conexão ao banco de dados fechada.")

    
    def select_contato(self, cnpj_cnpj_cliente:str):
        self.conn._open_connection()
        result = []
        result.clear()
        try:
            # Query SQL para buscar os registros na tabela com filtros opcionais
            sql_select_query = "SELECT * FROM contato WHERE cnpj_cliente = %s"
            
            cnpj_cli = [cnpj_cnpj_cliente]

            cursor = self.conn.cursor()
            cursor.execute(sql_select_query, cnpj_cli)
            result = cursor.fetchall()

            cursor.close()
            self.conn.close()
                
            return result

        except mysql.connector.Error as error:
            print(f"Erro ao conectar ou buscar dados no banco de dados: {error}")


    def update_contato(self, pid, cnpj_cnpj_cliente: str, nome: str, cargo: str, telefone, email):
        self.conn._open_connection()
        try:
            # Query SQL para atualizar o registro do contato
            sql_update_query = "UPDATE contato SET cnpj_cliente = %s, nome = %s, cargo = %s, telefone = %s, email = %s WHERE pid = %s"

            # Executando a query com os valores fornecidos
            cursor = self.conn.cursor()
            cursor.execute(sql_update_query, (cnpj_cnpj_cliente, nome, cargo, telefone, email, pid))
            self.conn.commit()

            cursor.close()
            self.conn.close()

        except mysql.connector.Error as error:
            print(f"Erro ao conectar ou atualizar dados no banco de dados: {error}")


    def delete_cliente(self, pid_contato:int):
        self.conn._open_connection()
        try:
            # Query SQL para deletar o cliente pelo ID
            sql_delete_query = "DELETE FROM contato WHERE pid = %s"

            # Executando a query com o valor do ID do cliente
            cursor = self.conn.cursor()
            cursor.execute(sql_delete_query, (pid_contato,))
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