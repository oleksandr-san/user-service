# Simple user service

## Development

1. `pip install poetry`
2. Install dependencies `cd` into the directory where the `pyproject.toml` is located then `poetry install`
3. Run the DB migrations via `poetry run ./run_migrations.sh`
4. Run the FastAPI server via `poetry run ./entrypoint.sh`
5. Open http://localhost:8001/

## Installation

### Kubernetes

1. `cd deploy`
2. `helm install user-service ./user-service`

## Testing

You might need to modify baseUrl variable in the collection according to the ingress IP of your deployment (or to localhost for local development).

1. `npm install newman` 
2. `newman run tests/user_service_smoke.postman_collection.json`