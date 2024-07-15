import requests as req

# Obtém o nome do usuário
nome = input('Qual seu nome: ')
print(f'Olá, {nome}!')

def createReq():        
    # Obtém o produto desejado
    query = input('Qual produto deseja pesquisar: ')
    
    # Define os parametros para a requisição
    params = {
        'q': query,
        'limit': 42
    }

    # URL base da API do Mercado Livre
    base_url = 'https://api.mercadolibre.com/sites/MLB/search'

    # Obtém a resposta da requisição GET à API
    return req.get(base_url, params=params)

def makeRequest(request):
    # Verifica se a requisição foi bem-sucedida
    if request.status_code == 200:
        datas = request.json()
        return datas
    else:
        print(f'Erro ao consultar a API: {request.status_code} - {request.text}')


# Cria a requisição
request = createReq()

# Instancia um objeto para armazenar o objeto do resultado
result = makeRequest(request)

print(result)