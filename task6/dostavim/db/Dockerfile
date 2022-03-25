FROM mysql:5.7

WORKDIR /scripts
COPY scripts/ /docker-entrypoint-initdb.d/

ENV MYSQL_ROOT_PASSWORD admin
ENV MYSQL_DATABASE dostavim
