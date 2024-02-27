-- postgresql
DROP DATABASE rentikusearchdb_dev;
CREATE DATABASE rentikusearchdb_dev;
-- create admin role/user
DROP ROLE rsadmin_dev;
CREATE ROLE rsadmin_dev WITH SUPERUSER LOGIN PASSWORD 'rentikusearchadminpwd';

DROP OWNED BY rsuser_dev;
DROP USER rsuser_dev;
CREATE USER rsuser_dev WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE rentikusearchdb_dev TO rsuser_dev;
