FROM postgres:14.11
 
RUN apt-get update -y \
  && apt-get install -y pgcli pspg \
  && apt-get clean
