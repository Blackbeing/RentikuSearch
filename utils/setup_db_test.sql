-- postgresql
DROP DATABASE rentikusearchdb_test;
CREATE DATABASE rentikusearchdb_test;
-- create admin role/user
DROP ROLE rsadmin_test;
CREATE ROLE rsadmin_test WITH SUPERUSER LOGIN PASSWORD 'rentikusearchadminpwd';

DROP OWNED BY rsuser_test;
DROP USER rsuser_test;
CREATE USER rsuser_test WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE rentikusearchdb_test TO rsuser_test;
