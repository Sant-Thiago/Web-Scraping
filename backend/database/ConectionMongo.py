import pymongo
import pymongo.errors
import urllib.parse

class ConectionMongo:
    def __init__(self):
        try:
            mongo_host = 'localhost'
            mongo_port = 27017
            mongo_user = urllib.parse.quote_plus('admin')
            mongo_password = urllib.parse.quote_plus('Senh4ForT3&S3GUr@')
            database_name = 'Web-Scraping'
            
            # url = 'mongodb+srv://Thiago123:Thiago123@tigoscluster.0nmjkid.mongodb.net/?appName=TigosCluster'

            # Criação do cliente MongoBD
            self.client = pymongo.MongoClient(f'mongodb://{mongo_user}:{mongo_password}@{mongo_host}:{mongo_port}/{database_name}?authSource=admin')
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

    # Necessario por conta do comando With ....
    def __enter__(self):
        return self

    # Necessario por conta do comando With ....
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
        