#!/bin/bash
set -ex

case $1 in
"--run"|"-r")
  docker-compose -f compose.yml up
  ;;
"--build"|"-b" )
  docker-compose -f compose.yml up --build
  ;;
"--test"|"-t" )
  export DOCKER_COMMAND="pytest -p no:cacheprovider"
  docker-compose -f compose.cmd.yml up --build --exit-code-from=backend
  ;;
"--check-lint"|"-c")
  export DOCKER_COMMAND="flake8 --max-line-length=150 --exclude=*migrations*,*__init__*,*settings*,*venv*,*base.py"
  docker-compose -f compose.cmd.yml up --build --exit-code-from=backend
  ;;
"--delete"|"-d")
  docker-compose -f compose.yml down --rmi local
  ;;
"--alembic"|"-a")
  export DOCKER_COMMAND="alembic upgrade head"
  docker-compose -f compose.cmd.yml up --build --exit-code-from=backend
*)
  echo " use ./build.sh -[r|b|t|c|d]"
  ;;
esac
