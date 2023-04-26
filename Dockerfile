# Derivando da imagem oficial do MySQL
From mysql:5.7

# Adicionando os script SQL para serem executados na criação do banco
COPY ./db/ /docker-entrypoint-initdb.d/