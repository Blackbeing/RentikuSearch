#!/usr/bin/bash

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

if [[ "$choice" == "dev" ]]
  psql -Ublackbeing -hdb -drentikusearchdb_dev -f ./setup_db_dev.sql
  exit 0;
fi
if [[ "$choice" == "test" ]]
  psql -Ublackbeing -hdb -drentikusearchdb_test -f ./setup_db_test.sql
  exit 0;
fi
;
