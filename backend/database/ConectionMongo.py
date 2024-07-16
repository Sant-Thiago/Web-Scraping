import pymongo
import pymongo.errors

class ConectionMongo:
    def __init__(self):
        try:
            url = 'mongodb+srv://Thiago123:Thiago123@tigoscluster.0nmjkid.mongodb.net/?appName=TigosCluster'

            # Criação do cliente MongoBD
            self.client = pymongo.MongoClient(url)
            print('[SUCESS] Conexão com MongoDB estabelecida com sucesso!')
        except pymongo.errors.ConnectionFailure as e:
            print(f'[ERROR] Erro ao conectar ao MongoBD: {e}')
            self.client = None

    def list(self):
        if self.client:
            return self.client.list_database_names()
        return[]
    
    def use(self, collection):
        if self.client:
            return self.client['Web-Scraping'][collection]
        return None

    def close(self):
        if self.client:
            self.client.close()
            print('[INFO] Conexão com MongoBD fechada.')