# FastAPI + PostgreSQL + SQLAlchemy + PGAdmin Docker Template
The RESTful API created using FastAPI, SQLAchemy, and PostgreSQL.
This project contains a sample homepage, a pre-configured FastAPI app, and a sample setup of SQLAlchemy + PostgreSQL.


## Run with Docker
- To run for development, navigate to the top level directory of the repo and run the command:
```bash
docker compose up
```

## Website and Docs
- Open a web browser and type in:
```
http://localhost:8080
```

## PGAdmin website
- Open a web browser and type in:
```
http://localhost:5050/browser/
```
- Once on the page, login using the default credentials (can be changed in [compose.yml](./compose.yml))
```yml
PGADMIN_DEFAULT_EMAIL: admin@localhost.com
PGADMIN_DEFAULT_PASSWORD: admin
```
- To connect to PostgreSQL database (after logging in), right-click on `Servers`.
- Click `Register > Server`.
- Under the `general` tab, write the desired name for the name field.
- Under the `connection` tab, type in `postgres-db` for the `hostname`. For the `port`, type in `5432`. For the `user`, type in `admin`.
- NOTE: These credentials / config can be changed in the [db_config.env](./db_config.env) file.
```bash
POSTGRES_USER=admin
POSTGRES_PASSWORD=password
POSTGRES_DB=database
POSTGRES_HOST=postgres-db
POSTGRES_PORT=5432
```

### NOTE: Disregard this, only applies to running locally / specifying the CMD to run in Docker
 - To run for development, run the command:
 ```bash
python -m uvicorn app.api:app --host 0.0.0.0 --port 8080 --reload
 ```

- To run for production, run the command:
```bash
python -m uvicorn app.api:app --host 0.0.0.0 --port 8080
```
