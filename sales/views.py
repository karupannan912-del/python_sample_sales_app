import json
from urllib.request import urlopen
from django.shortcuts import render

API_BASE = "http://127.0.0.1:8001"


def _fetch_json(path):
    try:
        with urlopen(f"{API_BASE}{path}", timeout=3) as response:
            return json.load(response)
    except Exception:
        return []


def home(request):
    return render(request, "home.html")


def dashboard(request):
    summary = _fetch_json("/sales-summary")
    if not summary:
        summary = {"total_sales": 0, "orders": 0, "customers": 0, "inventory_items": 0}
    return render(request, "dashboard.html", {"page": "Dashboard", "summary": summary})


def orders(request):
    orders_data = _fetch_json("/orders")
    return render(request, "orders.html", {"page": "Orders", "orders": orders_data})


def customers(request):
    customers_data = _fetch_json("/customers")
    return render(request, "customers.html", {"page": "Customers", "customers": customers_data})


def inventory(request):
    inventory_data = _fetch_json("/inventory")
    return render(request, "inventory.html", {"page": "Inventory", "inventory": inventory_data})


def reports(request):
    summary = _fetch_json("/sales-summary")
    if not summary:
        summary = {"total_sales": 0, "orders": 0, "customers": 0, "inventory_items": 0}
    return render(request, "reports.html", {"page": "Reports", "summary": summary})
