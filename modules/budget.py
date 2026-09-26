def calculate_remaining_budget(total_income: float, total_expenses: float) -> float:
    """Calculates remaining budget allowance."""
    return total_income - total_expenses

def check_budget_status(total_income: float, total_expenses: float) -> str:
    """Evaluates expenditure percentage against income limits."""
    if total_income <= 0:
        return "Invalid Income Specified"
    
    usage_percentage = (total_expenses / total_income) * 100
    
    if usage_percentage >= 100:
        return f"CRITICAL: Budget Exceeded! ({usage_percentage:.1f}% used)"
    elif usage_percentage >= 80:
        return f"WARNING: Approaching Budget Limit ({usage_percentage:.1f}% used)"
    else:
        return f"HEALTHY: Within Safe Budget Limits ({usage_percentage:.1f}% used)"
