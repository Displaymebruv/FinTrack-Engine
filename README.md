# FinTrack-Engine
# FinTrack - Personal Finance & Expense Analytics Engine

FinTrack is a modular Python CLI app built to track daily expenditures, monitor monthly budget limits, and calculate compound savings growth. It runs using pure Python 3 without requiring external third-party packages.

## Features
- **Budget Monitoring:** Shows remaining allowance and issues `WARNING` (at 80%) or `CRITICAL` (at 100%) status alerts.
- **Expense Analytics:** Computes total spend, average daily spend, highest spend, and lowest spend.
- **Savings Projection:** Calculates compound interest earnings year-by-year.
- **Modular Code:** Logic split cleanly across dedicated sub-modules.

## Non-Functional & System Specifications
- **Error Resilience:** Input loop wrapped in `try-except` to intercept invalid numeric types.
- **Boundary Safety:** Explicit guards against division by zero and empty expense lists.
- **Zero Dependencies:** Uses standard Python 3 syntax exclusively.
- **Clean Output:** Money values formatted with f-string precision (`₹{value:.2f}`).

## File Structure
```text
FinTrack-Engine/
├── main.py                # Main script and interactive CLI menu
├── statement.md           # Problem statement and system requirements
├── README.md              # Project setup and overview
├── modules/
│   ├── __init__.py        # Package initialization
│   ├── budget.py          # Budget checking & status warnings
│   ├── analytics.py       # Sum, average, max, and min math functions
│   └── interest.py        # Compound interest power calculations
└── tests/
    └── test_finance.py    # Basic unit test cases
