import sqlite3
conexao = sqlite3.connect('API-Imagens.db')
cursor = conexao.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS ImagensApi '
               '(ID INTEGER PRIMARY KEY, '
               'Descricao TEXT, Imagem TEXT)'

)