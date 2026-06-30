# Data Pipeline Project

This is my first ETL data pipeline project built with Python.

## Features

- Extracts user data from a public REST API
- Cleans and transforms the data using Pandas
- Loads the processed data into PostgreSQL using SQLAlchemy
- Uses environment variables for database credentials
- Uses uv for dependency management
- Includes Docker Compose for PostgreSQL

## Technologies

- Python
- Pandas
- SQLAlchemy
- PostgreSQL
- Docker
- uv

## Setup

```bash
git clone https://github.com/Poisonsouls/data-pipeline-project.git

cd data-pipeline-project

uv sync

docker compose up -d

uv run python project_pipeline.py
```

## Environment Variables

Create a `.env` file using `.env.example`.
