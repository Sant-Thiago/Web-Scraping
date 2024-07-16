FROM mongo:latest as builder

WORKDIR /app

COPY ./configMongo.sh /app/docker-entrypoint-initdb.d/

ENV MONGO_INITDB_ROOT_USERNAME="admin"
ENV MONGO_INITDB_ROOT_PASSWORD="Senh4ForT3&S3GUr@"

RUN chmod +x /app/docker-entrypoint-initdb.d/configMongo.sh

EXPOSE 27017

## Inicia o serviço do MongoDB (não é necessário, a imagem oficial do MongoDB já faz isso)
# CMD ["mongod"]

# Execute o script de inicialização durante a construção da imagem
CMD ["--auth"]
