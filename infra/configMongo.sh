#!/bin/bash

database='Web-Scraping'
collections=('User' 'Product');

# Inicia o serviço do MongoDB
service mongod start

# Cria um usuário administrador
mongo admin --eval "db.createUser({ user: 'admin', pwd: 'Senh4ForT3&S3GUr@', roles: [{ role: 'root', db: 'admin' }] })"

# Cria o banco de dados
mongo $database --eval "db.createUser({ user: 'lilUser', pwd: 'LilUser123', roles: [{ role: 'readWrite', db: '$database' }] })"

# Cria as coleções
for collection in "${collections[@]}"; do
    mongo $database --eval "db.createCollection('$collection)"
done

## Importa dados iniciais
# mongoimport --db $database --collection User --file /data/init/users.json --jsonArray

# Encerra o serviço do MongoDB
service mongod stop