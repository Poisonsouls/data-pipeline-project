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

Before running the project, create a `.env` file by copying `.env.example`.

**Linux/macOS/Git Bash**

```bash
cp .env.example .env
```

**PowerShell**

```powershell
Copy-Item .env.example .env
```

Then update the values in `.env` with your PostgreSQL credentials.

Example:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=company
DB_USER=your_username
DB_PASSWORD=your_password
```
