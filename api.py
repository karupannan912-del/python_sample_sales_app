from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Sales API")

class SalesSummary(BaseModel):
    total_sales: float
    orders: int
    customers: int
    inventory_items: int


def get_sales_summary():
    return {
        "total_sales": 125430.75,
        "orders": 184,
        "customers": 67,
        "inventory_items": 320,
    }


def get_orders():
    return [
        {"id": 1001, "customer": "Ava Patel", "amount": 1250.0, "status": "Paid"},
        {"id": 1002, "customer": "Noah Kim", "amount": 890.5, "status": "Pending"},
        {"id": 1003, "customer": "Mia Chen", "amount": 2140.0, "status": "Paid"},
    ]


def get_customers():
    return [
        {"id": 1, "name": "Ava Patel", "email": "ava@example.com", "city": "Seattle"},
        {"id": 2, "name": "Noah Kim", "email": "noah@example.com", "city": "Austin"},
        {"id": 3, "name": "Mia Chen", "email": "mia@example.com", "city": "Chicago"},
    ]


def get_inventory():
    return [
        {"sku": "SKU-100", "name": "Laptop", "stock": 24, "price": 999.0},
        {"sku": "SKU-101", "name": "Monitor", "stock": 15, "price": 249.0},
        {"sku": "SKU-102", "name": "Mouse", "stock": 48, "price": 29.0},
    ]


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/sales-summary", response_model=SalesSummary)
def sales_summary():
    return get_sales_summary()


@app.get("/orders")
def orders():
    return get_orders()


@app.get("/customers")
def customers():
    return get_customers()


@app.get("/inventory")
def inventory():
    return get_inventory()
