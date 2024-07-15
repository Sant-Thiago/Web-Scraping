import pymongo
import pymongo.errors

class ConectionMongo:
    def __init__(self):
        try:
            url = 'mongodb+srv://Thiago123:Mari2013@tigoscluster.0nmjkid.mongodb.net/?appName=TigosCluster'

            # Criação do cliente MongoBD
            self.client = pymongo.MongoClient(url)
            print('Conexão com MongoDB estabelecida com sucesso!')
        except pymongo.errors.ConnectionFailure as e:
            print(f'Erro ao conectar ao MongoBD: {e}')
            self.client = None

    def listar(self):
        if self.client:
            return self.client
        return[]

    def close(self):
        if self.client:
            self.client.close()
            print('Conexão com MongoBD fechada.')