def final_total(subtotal_cents: int, loyalty: bool = False) -> int:
    """Return the final total in integer cents (see spec.md)."""
    if subtotal_cents <= 0:
        raise ValueError("subtotal must be greater than 0")
    if subtotal_cents >= 10000:
        tier = 10
    elif subtotal_cents >= 5000:
        tier = 5
    else:
        tier = 0
    total = subtotal_cents - subtotal_cents * tier // 100
    if loyalty:
        total = total - total * 2 // 100
    return total
