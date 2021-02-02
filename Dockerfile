FROM mysql:8.0.23

ENV MYSQL_DATABASE classicmodels
ENV MYSQL_ROOT_PASSWORD root
ENV MYSQL_USER kevin
ENV MYSQL_PASSWORD motdepasse

COPY ./bdd.sql ./docker-entrypoint-initdb.d/

EXPOSE 3306