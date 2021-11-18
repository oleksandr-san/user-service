#!/bin/sh
set -e

# Default values of arguments
SHOULD_RUN_MIGRATIONS=0

# Loop through arguments and process them
for arg in "$@"
do
    case $arg in
        -m|--run-migrations)
        SHOULD_RUN_MIGRATIONS=1
        shift # Remove flag from processing
        ;;
        *)
        shift # Remove generic argument from processing
        ;;
    esac
done

. /venv/bin/activate

# Let the DB start
python -m app.backend_pre_start

if [ $SHOULD_RUN_MIGRATIONS -eq 1 ]; then
    sh ./run_migrations.sh
fi

export APP_MODULE=${APP_MODULE-app.main:app}
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8001}

exec uvicorn --host $HOST --port $PORT "$APP_MODULE"