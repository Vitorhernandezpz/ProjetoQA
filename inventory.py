def remaining_stock(available: int, quantity: int) -> int:
    """Return the balance after a purchase, given a nonnegative stock count."""
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    if quantity > available:
        raise ValueError("Insufficient stock")
    return available - quantity
