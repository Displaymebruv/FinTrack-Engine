def calculate_remaining_budget(total_income: float, total_expenses: float) -> float:
    return total_income - total_expenses
def budget_status(total_income: float,total_expenses: float) -> str:
    if total_income <=0:
        return "Invalid Value Given"

    percentage = (total_expenses/total_income)*100

    if percentage >= 100:
        return f"CRITICAL Budget Exceeded!({percentage:.1f})% used)"
    elif percentage >= 80:
        return f"WARNING Approaching Budget Limit!!({percentage:.1f}% used)"
    else:
        return f"HEALTHY within Safe Budget Limits!!!({percentage:.1f}% used)"