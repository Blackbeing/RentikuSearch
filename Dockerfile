FROM python:3.10

WORKDIR /RentikuSearch

COPY pyproject.toml pdm.lock /RentikuSearch

RUN pip install --no-cache-dir --upgrade RentikuSearch/

COPY ./RentikuSearch/ /RentikuSearch

CMD ["python", "manage.py", "api", "--host", "0.0.0.0", "--port", "5050"]
CMD ["python", "manage.py", "web", "--host", "0.0.0.0", "--port", "80"]
