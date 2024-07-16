from flask import Blueprint, request, jsonify
from database.ConectionMongo import ConectionMongo 

# Cria um Blueprint
app = Blueprint('DynamicController', __name__)

# Endpoint para criar dinamicamente
@app.route('/create/wsdata', methods=['POST'])
def dynamicCreate():
    try:
        # Obtém a collection dos parametros do URL
        collectionName = request.args.get('collection')
        if not collectionName:
            raise ValueError('Parâmetro "collection" não especificada')
        
        # Obtém os dados JSON enviados na requisição POST
        data = request.json
        
        # Cria um contexto de gerenciamento
        with ConectionMongo() as con:
            # Conectando e usando a coleção
            collection = con.use(collectionName)
            if collection is None:
                return jsonify({'error': f'Coleção "{collectionName}" não encontrado!'}), 404

            # Executando a inserção
            result = collection.insert_one(data)
            if result.inserted_id:
                return jsonify({'message': 'Registro criado com sucesso!', 'id': str(result.inserted_id)}), 201
            else:
                return jsonify({'message': 'Erro ao criar registro!'}), 500
            
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    
    except Exception as e:
        return jsonify({'error': 'Erro interno no servidor', 'exception': str(e)}), 500


# Endpoint para selecionar dinamicamente
@app.route('/select/wsdata', methods=['GET'])
def dynamicSelectAll():
    try:
        # Obtém a collection dos parametros do URL
        collectionName = request.args.get('collection')
        if not collectionName:
            raise ValueError('Parâmetro "collection" não especificada')
        
        # Cria um contexto de gerenciamento
        with ConectionMongo() as con:
            # Conectando e usando a coleção
            collection = con.use(collectionName)
            if collection is None:
                return jsonify({'error': f'Coleção "{collectionName}" não encontrado!'}), 404

            # Seleciona tudo
            records = list(collection.find({}))

            # Converte ObjectId para String
            for record in records:
                record['_id'] = str(record['_id'])

            return jsonify(records), 200
    
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    
    except Exception as e:
        return jsonify({'error': 'Erro interno no servidor', 'exception': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
