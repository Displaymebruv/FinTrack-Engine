# modules/budget.py

def calculate_remaining_budget(inc: float, exp: float) -> float:
    return inc - exp

def budget_status(inc: float, exp: float) -> str:
    if inc <= 0:
        return "Invalid Value Given"

    pct = (exp / inc) * 100

    if pct >= 100:
        return f"CRITICAL Budget Exceeded! ({pct:.1f}% used)"
    elif pct >= 80:
        return f"WARNING Approaching Budget Limit!! ({pct:.1f}% used)"
    else:
        return f"HEALTHY within Safe Budget Limits!!! ({pct:.1f}% used)"
