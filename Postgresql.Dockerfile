FROM postgres:14.11
 
RUN apt-get update -y \
  && apt-get install -y pgcli pspg \
  && apt-get clean

COPY ./utils/setup_db_dev.sql /docker-entrypoint-initdb.d/
