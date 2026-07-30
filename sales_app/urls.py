from django.contrib import admin
from django.urls import path
from sales import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("orders/", views.orders, name="orders"),
    path("customers/", views.customers, name="customers"),
    path("inventory/", views.inventory, name="inventory"),
    path("reports/", views.reports, name="reports"),
]
