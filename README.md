# FastAPI Data Lab

This project is a practical FastAPI learning API focused on data, business indicators, and simple frontend testing.

It exposes several `GET` endpoints that simulate corporate data use cases such as sales indicators, inactive customers, logistics lead time, production summary, and financial summary.

## Project Structure

```text
FastApi/
  main.py
  frontend/
    index.html
    style.css
    script.js
```

## Requirements

- Python 3.10 or newer
- FastAPI
- Uvicorn

Install the dependencies:

```bash
pip install fastapi uvicorn
```

If `pip` is not available directly, use:

```bash
python -m pip install fastapi uvicorn
```

## How to Run

Run the API from the project root:

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## Frontend

Open the frontend in the browser:

```text
http://127.0.0.1:8000/
```

The frontend provides buttons to call each endpoint and display the JSON response.

## API Documentation

FastAPI automatically generates interactive documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## Endpoints

### Health Check

```text
GET /status
```

Returns the API status.

### API Version

```text
GET /versao
```

Returns the current API name and version.

### Sales Indicators

```text
GET /indicadores/vendas
```

Returns simulated sales indicators such as total revenue, order count, average ticket, and period.

### Inactive Customers

```text
GET /clientes/inativos
```

Returns a list of inactive customers with days since last purchase and last purchase date.

### Logistics Lead Time

```text
GET /logistica/lead-time
```

Returns simulated logistics performance data for a route.

### Production Summary

```text
GET /producao/resumo
```

Returns simulated production data such as produced volume, rejected volume, efficiency, and period.

### Financial Summary

```text
GET /financeiro/resumo
```

Returns simulated financial data such as revenue, expenses, net profit, margin, and period.

## Current Purpose

This project is intentionally simple. The goal is to learn FastAPI by building practical endpoints before adding more advanced topics such as:

- request parameters
- request bodies
- Pydantic validation
- project organization
- database integration
- authentication
- machine learning model serving
- deployment
