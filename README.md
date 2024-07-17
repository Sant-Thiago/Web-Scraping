# Web-Scraping

Este repositório contém um exemplo de aplicação CRUD (Create, Read, Update, Delete) utilizando MongoDB como banco de dados, Flask para o backend em Python e React para o frontend.

## Estrutura do Projeto

- **Backend (Flask)**: Implementa uma API RESTful com endpoints dinâmicos para operações CRUD em um banco de dados MongoDB. Utiliza a biblioteca pymongo para interagir com o MongoDB.

- **Frontend (React)**: Fornece uma interface web interativa onde os usuários podem se autenticar, cadastrar novos usuários, realizar buscas de produtos e exibir resultados obtidos através da API do Mercado Livre.

## Funcionalidades Principais

1. **Endpoints da API (Flask)**:

   - `/create/wsdata` (POST): Cria um novo documento em uma coleção específica.
   - `/select/wsdata` (GET): Retorna todos os documentos de uma coleção.
   - `/select/wsdata/by` (GET): Retorna um documento específico com base em um parâmetro dinâmico (exemplo: CPF).
   - `/update/wsdata` (PUT): Atualiza um documento com base no ID especificado.
   - `/delete/wsdata` (DELETE): Deleta um documento com base no ID especificado.

2. **Integração com API Externa**:
   
   - Utiliza a API do Mercado Livre para buscar produtos com base em um termo específico inserido pelo usuário na página de busca.

## Como Executar o Projeto

1. **Backend (Flask)**:

   - Certifique-se de ter o Python e o Flask instalados.
   - Instale as dependências do Python com `pip install -r requirements.txt`.
   - Inicie o servidor Flask com `python app.py`.

2. **Frontend (React)**:

   - Certifique-se de ter o Node.js e o npm instalados.
   - Navegue até o diretório `frontend` e instale as dependências com `npm install`.
   - Inicie o servidor de desenvolvimento com `npm start`.

## Tecnologias Utilizadas

- **Flask**: Framework web em Python para construção do backend.
- **React**: Biblioteca JavaScript para construção da interface de usuário.
- **MongoDB**: Banco de dados NoSQL utilizado para armazenamento de dados.

## Contribuição

Contribuições são bem-vindas! Para sugestões ou problemas encontrados, abra uma issue neste repositório.

---

Desenvolvido por [Sant-Thiago](https://github.com/Sant-Thiago)
