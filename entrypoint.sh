#!/bin/sh
set -e

. /venv/bin/activate

# Let the DB start
python -m app.backend_pre_start

# Run migrations
alembic upgrade head

# Create initial data in DB
# python ./app/initial_data.py

export APP_MODULE=${APP_MODULE-app.main:app}
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8001}

exec uvicorn --host $HOST --port $PORT "$APP_MODULE"