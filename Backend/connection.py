from mysql.connector import connect

class Connection:
    host:str
    user:str
    passwd:str
    database:str

    def __init__(self, host:str, user:str, passwd:str, database:str):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database

    def get_connection(self):
        connection = connect(
            host = self.host,
            user = self.user,
            passwd = self.passwd,
            database = self.database
        )
        return connection