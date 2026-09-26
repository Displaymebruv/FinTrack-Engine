def calculate_remaining_budget(total_income: float, total_expenses: float) -> float:
    """calculates the leftover allowance"""
    return total_income - total_expenses
def budget_status(total_income: float,total_expenses: float) -> str
    """Evaluates expenditure percentage against income limits."""
    if total_income <=0:
        return "Invalid Invalid Given"

    percentage = (total_expenses/total-income)*100
    
    if percentage >= 100:
        return f"CRITICAL Budget Exceeded!({percentage :.if}% used)"
    elif percentage >= 80:
        return f "WARNING Approaching Budget Limit!!({percentage:.1f}% used)
    else:
        return f"HEALTHY within Safe Budget Limits!!!({percentage:.1f}% used)"
