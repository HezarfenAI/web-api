# WebAPI Project For Data Sending to UI From AI Model

## Getting Started

First, you need to install the required dependencies. You can do this by running the following command:

```bash
pip install -r requirements.txt
```

and then you have to create a new database with the following command:

```bash
docker run --name hezarfen_db -e POSTGRES_PASSWORD=hezarfen123- -e POSTGRES_USER=postgres -p 5432:5432 postgres
```

## Usage

To run the web API, execute the following command:

```bash
python src/server.py
```

## Updating Depenedencies

```bash
pip freeze > requirements.txt
```

## Installing Dependencies

```bash
pip install -r requirements.txt
```

## Database Operations

### Creating a new migration

```bash
alembic revision --autogenerate -m "initial migration"
```

### Applying migrations

```bash
alembic upgrade head
```

### Dropping the database

```bash
docker stop hezarfen_db
docker rm hezarfen_db
```

### Creating a new database

```bash
docker run --name hezarfen_db -e POSTGRES_PASSWORD=hezarfen123- -e POSTGRES_USER=postgres -p 5432:5432 postgres
```
