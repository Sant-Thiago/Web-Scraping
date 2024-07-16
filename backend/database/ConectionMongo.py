import pymongo
import pymongo.errors

class ConectionMongo:
    def __init__(self):
        try:
            mongo_host = '172.17.0.2'
            mongo_port = 27017
            mongo_user = 'lilUser'
            mongo_password = 'LilUser123'
            database_name = 'Web-Scraping'
            
            # url = 'mongodb+srv://Thiago123:Thiago123@tigoscluster.0nmjkid.mongodb.net/?appName=TigosCluster'

            # Criação do cliente MongoBD
            self.client = pymongo.MongoClient(f'mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/{database_name}')
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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        