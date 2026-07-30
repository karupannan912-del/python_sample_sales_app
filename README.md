# Simple Sales App

This project contains:
- Django frontend with 6 navigation tabs: Home, Dashboard, Orders, Customers, Inventory, and Reports
- FastAPI backend with simple sales summary API endpoints

## Run the Django app

```bash
python manage.py runserver 0.0.0.0:8000
```

## Run the FastAPI app

```bash
uvicorn api:app --reload --port 8001
```

Open:
- Django UI: http://localhost:8000
- FastAPI docs: http://localhost:8001/docs
