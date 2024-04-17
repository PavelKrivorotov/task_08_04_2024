# !/bin/bash

# set workdir
cd ./src

# run migrations
alembic upgrade head

# run app
python manage.py
