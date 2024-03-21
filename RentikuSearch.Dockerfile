FROM python:3.10

WORKDIR /RentikuSearch

COPY pyproject.toml .

RUN pip install --no-cache-dir --upgrade  .

RUN  apt-get update -y && apt-get install postgresql-client -y

COPY . .

CMD ["bash", "run_services.sh"]
