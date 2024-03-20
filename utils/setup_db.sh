#!/usr/bin/bash
 
HERE="$(dirname "$(readlink -fn "$0")")"
DEV_SCRIPT="$HERE/setup_db_dev.sql"
TEST_SCRIPT="$HERE/setup_db_test.sql"
# check if psql is installed
if [[ ! -x "$(command -v psql)" ]]; then
  echo "Error: psql is not installed." >&2
  exit 1
fi
choices=("dev" "test")
choice=$1
 
if [[ -z "$choice" ]]; then
  echo "Please choose a database to setup. Options: ${choices[@]}"
  exit 1;
fi
 
if [[ "$choice" == "dev" ]]; then
  PGPASSWORD=password psql -Ublackbeing -hdb postgres -f "$DEV_SCRIPT"
  # get parent directory
  cd "$(dirname $HERE)"
  alembic upgrade head
  cd -
  exit 0;
fi
if [[ "$choice" == "test" ]]; then
  PGPASSWORD=password psql -Ublackbeing -hdb postgres -f "$TEST_SCRIPT"
  cd "$(dirname $HERE)"
  alembic upgrade head
  cd -
  exit 0;
fi
;

