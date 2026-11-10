import pytest

from inventory import remaining_stock


@pytest.mark.parametrize(
    ("quantity", "expected"), [(1, 4), (4, 1), (5, 0)],
    ids=["one-unit", "below-stock", "exact-stock"],
)
def test_purchase_returns_remaining_stock(quantity, expected):
    assert remaining_stock(5, quantity) == expected


@pytest.mark.parametrize("quantity", [-1, 0])
def test_purchase_requires_positive_quantity(quantity):
    with pytest.raises(ValueError, match="Quantity must be positive"):
        remaining_stock(5, quantity)


@pytest.mark.parametrize(("available", "quantity"), [(5, 6), (0, 1)])
def test_purchase_rejects_insufficient_stock(available, quantity):
    with pytest.raises(ValueError, match="Insufficient stock"):
        remaining_stock(available, quantity)
