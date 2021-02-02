FROM mysql:8.0.23

ENV MYSQL_DATABASE classicmodels

COPY ./bdd.sql ./docker-entrypoint-initdb.d/

EXPOSE 3306