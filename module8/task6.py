educational_grant = float(input("Введите стипендию: "))
expenses = float(input("Введите расходы на проживание: "))
 
monthly_increase = 0.03
total_shortfall = 0
current_expenses = expenses

for month in range(1, 11):
    shortfall = current_expenses - educational_grant
    if shortfall > 0:
        total_shortfall += shortfall
    print(f"месяц {month} траты {current_expenses:.2f} не хватает {shortfall:.2f}")
    current_expenses *= (1 + monthly_increase)

print(f"Нужно попросить у родителей {total_shortfall:.2f} рублей")
