# Shipment Management API

A simple **FastAPI REST API** for managing shipments using an in-memory Python dictionary as a mini database.

## Features

- **GET** — Retrieve a shipment
- **POST** — Add a new shipment
- **PUT** — Replace shipment details
- **PATCH** — Update specific shipment fields
- **DELETE** — Delete a shipment
- Basic validation and HTTP error handling
- Scalar API documentation

## Tech Stack

- Python
- FastAPI
- Scalar
- Uvicorn

## Run the API

Install dependencies:

```bash
uv add fastapi scalar-fastapi uvicorn
```

Start the server:

```bash
uv run uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

Scalar documentation:

```text
http://127.0.0.1:8000/scalar
```

FastAPI OpenAPI docs:

```text
http://127.0.0.1:8000/docs
```

## Example Requests

Get the latest shipment:

```text
GET /shipment
```

Get a specific shipment:

```text
GET /shipment?id=12701
```

Add a shipment:

```text
POST /shipment?weight=15
```

## Note

This project uses an **in-memory dictionary**, so data will be lost when the application restarts.

It is intended as a small project for practising **FastAPI, REST APIs, HTTP methods, validation and error handling**.
