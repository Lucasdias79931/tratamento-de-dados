import mysql.connector

class Conexao:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def conectar(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password,
            )
            print("\nConectou com sucesso")
        except mysql.connector.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def desconectar(self):
        if self.connection is not None:
            self.connection.close()
            print("\nDesconectado")

    def query(self, query, valores=None):
        try:
            cursor = self.connection.cursor()
            if valores:
                cursor.execute(query, valores)
            else:
                cursor.execute(query)
        
            return cursor
        except mysql.connector.Error as e:
            print(e)
