FROM python:3.10

WORKDIR /RentikuSearch

COPY pyproject.toml .

RUN pip install --no-cache-dir --upgrade  .

RUN  apt-get update -y && apt-get install postgresql-client -y

COPY . .

CMD ["python", "manage.py", "api", "--host", "0.0.0.0", "--port", "5050"]
CMD ["python", "manage.py", "web", "--host", "0.0.0.0", "--port", "80"]
