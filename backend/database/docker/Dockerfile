FROM mongo

ENV MONGO_INITDB_ROOT_USERNAME="admin"
ENV MONGO_INITDB_ROOT_PASSWORD="Senh4ForT3&S3GUr@"

EXPOSE 27017

# mongod: Inicia o serviço do MongoDB (não é necessário, a imagem oficial do MongoDB já faz isso)
# --auth: Execute o script de inicialização durante a construção da imagem
CMD ["mongod", "--auth"]
