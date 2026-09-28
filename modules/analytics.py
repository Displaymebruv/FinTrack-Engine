def calculate_total_expenses(expenses: list) -> float:
    total = 0.0
    for amount in expenses:
        total += amount
    return total

def calculate_average_expense(expenses: list) -> float:
    if not expenses:
        return 0.0
    return calculate_total_expenses(expenses) / len(expenses)

def find_highest_expense(expenses: list) -> float:
    if not expenses:
        return 0.0
    highest = expenses[0]
    for amount in expenses:
        if amount > highest:
            highest = amount
    return highest

def find_lowest_expense(expenses: list) -> float:
    if not expenses:
        return 0.0
    lowest = expenses[0]
    for amount in expenses:
        if amount < lowest:
            lowest = amount
    return lowest
