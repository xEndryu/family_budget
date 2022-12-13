# Family Budget application

Service based on fastAPI with postgres database.

Provides swagger at <localhost:8000/docs>

## Requirements

- docker(<https://docs.docker.com/get-docker/>)
- docker-compose(<https://docs.docker.com/compose/install/>)

## Tech stack

- Python 3.10
- fastAPI
- uvicorn
- psycopg2
- SQLAlchemy
- Alembic
- pytest

## How to run - Local Development environment

All the deployment is done by using the `build.sh` script. Below you can find it's arguments:

- -r | --run : run app
- -b | --build : same as above but docker-compose is invoked with --build
- -t | --test : run pytest
- -c | --check-lint : check linting
- -d | --delete : delete images and networks
- -a | --alembic : run alembic migration
