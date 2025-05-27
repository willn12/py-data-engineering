# Fannie Mae Data Engineering Demo

This project demonstrates data engineering skills through a housing and mortgage data pipeline. It showcases Python programming, data processing, API development, and data visualization capabilities.

I wanted to create this project to help demonstrate a knowledge of python and data engineering

## Features

- Data ingestion from public housing datasets
- ETL pipeline for data transformation and cleaning
- FastAPI backend with RESTful endpoints
- DuckDB for efficient data storage
- Unit tests with pytest

## Setup Instructions

1. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python run.py
   ```

## Using the Application

1. After running `python run.py`, the application will:
   - Generate sample loan data in the `data` directory
   - Start the FastAPI server

2. Open your browser and go to: http://localhost:8000/docs

3. In the Swagger UI:
   - Click on the `/process-loans` endpoint
   - Click "Try it out"
   - Click "Choose File"
   - Select the generated CSV file from `data/sample_loan_data.csv`
   - Click "Execute"

4. The API will return:
   - A success message
   - Calculated metrics (total loans, average amounts, etc.)
   - A sample of the cleaned data

## Project Structure

```
py-data-engineering/
├── data/                  # Data storage directory
├── src/                   # Source code
│   ├── api/              # FastAPI application
│   ├── etl/              # ETL pipeline components
│   ├── models/           # Data models and schemas
│   └── utils/            # Utility functions
├── tests/                # Test files
└── requirements.txt      # Project dependencies
```
## License
MIT License 