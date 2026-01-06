from fastapi import FastAPI
from routers import sales

app = FastAPI(
    title="Predictive Analytics API",
    description="FastAPI + psycopg2 + PostgreSQL",
    version="1.0.0"
)

app.include_router(sales.router)