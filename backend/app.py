import flask    
from database.ConectionMongo import ConectionMongo 

con = ConectionMongo()

dbs = con.listar()

try:
    dbs = con.listar()
    print(f'Bancos de dados: {dbs}')
except Exception as e:
    print(f"Erro ao listar bancos de dados: {e}")

con.close()