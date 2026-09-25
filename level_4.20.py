# Create a Monthly Expense Calculator that accepts monthly income and expenses for rent, food, travel,
# education, and entertainment. Display total expenses, remaining balance, and percentage of income spent.

monthly_income = float(input("Enter your monthly income: "))
rental_exp = float(input("Enter your rental expenses : "))
food_exp = float(input("Enter your food expenses : "))
travel_exp = float(input("Enter your travel expenses : "))
educational_exp = float(input("Enter your educational expenses : "))
entertainment_exp = float(input("Enter your entertainment expenses : "))

total_expenses = rental_exp + food_exp + travel_exp + educational_exp + entertainment_exp
remaining_balance = monthly_income - total_expenses
if monthly_income > 0:
    spent_percent = (total_expenses / monthly_income) * 100
else:
    spent_percent = 0.0

print(f"""
========== MONTHLY EXPENSE CALCULATOR ==========

Total expenses      : {total_expenses}
{"---" * 20}
Remaining Balance   : {remaining_balance}
{"---" * 20}
Spent Income %      : {spent_percent}
{"---" * 20}
""")