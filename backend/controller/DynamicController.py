from flask import Flask, request, jsonify
from database.ConectionMongo import ConectionMongo 

app = Flask(__name__)

# Endpoint para criar dinamicamente
@app.route('/create/wsdata', methods=['POST'])
def dynamicCreate():
    try:
        con = ConectionMongo()
        # Obtém a collection dos parametros do URL
        collectionName = request.args.get('collection')
        if not collectionName:
            raise ValueError('Parâmetro "collection" não especificada')
        
        # Obtém os dados JSON enviados na requisição POST
        data = request.json
        
        # Executando a inserção
        collection = con.use(collectionName)
        if not collection:
            return jsonify({'error': f'Coleção "{collectionName}" não encontrado!'}), 404

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


if __name__ == '__main__':
    app.run(debug=True)
