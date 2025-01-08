monthly_income = float(input("Enter yourmonthly income: "))
total_monthly_expenses = float(input("Enter your total monthlyexpenses: "))
monthly_saving = monthly_income-total_monthly_expenses
rate = 0.05
projected_saving = monthly_saving * 12 + monthly_saving * 12 * 0.05

print("Your monthly savings are", monthly_saving)
print("Projected savings after one year, with interest, is:", projected_saving)
