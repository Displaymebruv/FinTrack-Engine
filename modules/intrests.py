def compute_compound_interest(principal: float, rate: float, time_years: int) -> float:
    amount = principal
    multiplier = 1.0 + (rate / 100.0)
    
    for _ in range(time_years):
        amount *= multiplier
        
    return amount

def compute_interest_earned(principal: float, final_amount: float) -> float:
    return final_amount - principal
