#!/bin/sh
set -e

. /venv/bin/activate

# Let the DB start
python -m app.backend_pre_start

# Run migrations
alembic upgrade head
