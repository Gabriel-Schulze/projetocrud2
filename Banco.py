import mysql.connector

class Banco():
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host= "localhost",
            user= "root",
            password= "root",
            database= "gabrieleduardo_db" 
        )
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS tb_usuario(
            id_usuario INT AUTO INCREMENT PRIMARY KEY, 
            nome TEXT,
            telefone TEXT,
            email TEXT,
            usuario TEXT,
            senha TEXT                    
        );''')
        self.conexao.commit()
        c.close()