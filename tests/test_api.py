from api import get_customers, get_orders, get_sales_summary


def test_sales_summary_contains_expected_keys():
    summary = get_sales_summary()
    assert summary["total_sales"] > 0
    assert summary["orders"] > 0
    assert summary["customers"] > 0


def test_orders_endpoint_returns_rows():
    orders = get_orders()
    assert len(orders) >= 3
    assert orders[0]["id"] == 1001


def test_customers_endpoint_returns_rows():
    customers = get_customers()
    assert len(customers) >= 3
    assert customers[0]["name"] == "Ava Patel"
