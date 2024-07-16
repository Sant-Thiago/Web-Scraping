from flask import Blueprint, request, jsonify
from bson import ObjectId
from database.ConectionMongo import ConectionMongo 

# Cria um Blueprint
app = Blueprint('DynamicController', __name__)

# Endpoint para criar dinamicamente
@app.route('/create/wsdata', methods=['POST'])
def dynamicCreate():
    try:
        # Obtém a collection dos parametros do URL
        collection_name = request.args.get('collection')
        if not collection_name:
            raise ValueError('Parâmetro "collection" não especificada')
        
        # Obtém os dados JSON enviados na requisição POST
        data = request.json
        
        # Cria um contexto de gerenciamento
        with ConectionMongo() as con:
            # Conectando e usando a coleção
            collection = con.use(collection_name)
            if collection is None:
                return jsonify({'error': f'Coleção "{collection_name}" não encontrado!'}), 404

            # Executando a inserção
            result = collection.insert_one(data)
            if result.inserted_id:
                return jsonify({'message': 'Documento criado com sucesso!', 'id': str(result.inserted_id)}), 201
            else:
                return jsonify({'message': 'Erro ao criar documento!'}), 500
            
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    
    except Exception as e:
        return jsonify({'error': 'Erro interno no servidor', 'exception': str(e)}), 500


# Endpoint para selecionar dinamicamente
@app.route('/select/wsdata', methods=['GET'])
def dynamicSelectAll():
    try:
        # Obtém a collection dos parametros do URL
        collection_name = request.args.get('collection')
        if not collection_name:
            raise ValueError('Parâmetro "collection" não especificada')
        
        # Cria um contexto de gerenciamento
        with ConectionMongo() as con:
            # Conectando e usando a coleção
            collection = con.use(collection_name)
            if collection is None:
                return jsonify({'error': f'Coleção "{collection_name}" não encontrado!'}), 404

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

# Endpoint para atualizar dinamicamente
@app.route('/update/wsdata', methods=['PUT'])
def dynamicUpdate():
    try:
        # Obtém a collection dos parametros do URL
        collection_name = request.args.get('collection')
        if not collection_name:
            raise ValueError('Parâmetro "collection" não especificada')
        
        # Obtém a id dos parametros do URL
        document_id = request.args.get('id')
        if not document_id:
            raise ValueError('Parâmetro "id" não especificado')
        
        # Obtém os dados JSON enviados na requisição POST
        data = request.json
        
        # Cria um contexto de gerenciamento
        with ConectionMongo() as con:
            # Conectando e usando a coleção
            collection = con.use(collection_name)
            if collection is None:
                return jsonify({'error': f'Coleção "{collection_name}" não encontrado!'}), 404

            # Conta quantidade de documentos pelo id
            count_documents = collection.count_documents({ '_id': ObjectId(document_id) })
            if count_documents == 0:
                return jsonify({'message': f'Documento com o ID:: "{document_id}" não encontrado na coleção "{collection_name}"!' }), 404

            # Executando a inserção
            result = collection.update_one({ '_id': ObjectId(document_id) }, { '$set': data })
            if result.modified_count > 0:
                return jsonify({ 'message': 'Documento atualizado com sucesso!' }), 200
            else:
                return jsonify({ 'message': 'Erro ao atualizar documento!' }), 500
            
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    
    except Exception as e:
        return jsonify({'error': 'Erro interno no servidor', 'exception': str(e)}), 500


# Endpoint para deletar dinamicamente
@app.route('/delete/wsdata', methods=['DELETE'])
def dynamicDelete():
    try:
        # Obtém a collection dos parametros do URL
        collection_name = request.args.get('collection')
        if not collection_name:
            raise ValueError('Parâmetro "collection" não especificada')
        
        # Obtém a id dos parametros do URL
        document_id = request.args.get('id')
        if not document_id:
            raise ValueError('Parâmetro "id" não especificado')

        # Cria um contexto de gerenciamento
        with ConectionMongo() as con:
            # Conectando e usando a coleção
            collection = con.use(collection_name)
            if collection is None:
                return jsonify({'error': f'Coleção "{collection_name}" não encontrado!'}), 404

            # Conta quantidade de documentos pelo id
            count_documents = collection.count_documents({ '_id': ObjectId(document_id) })
            if count_documents == 0:
                return jsonify({'message': f'Documento com o ID:: "{document_id}" não encontrado na coleção "{collection_name}"!' }), 404

            # deleta documento
            result = collection.delete_one({ '_id': ObjectId(document_id) })
            if result.deleted_count > 0:
                return jsonify({ 'message': 'Documento deletado com sucesso!' }), 200
            else:
                return jsonify({ 'message': 'Erro ao deletar documento!' }), 500
    
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    
    except Exception as e:
        return jsonify({'error': 'Erro interno no servidor', 'exception': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
