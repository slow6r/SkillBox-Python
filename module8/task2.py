number_of_debtors = int(input("Введите количество должников: "))
total_debt = 0

for debtor_index in range(0, number_of_debtors, 5):
    print(f"Должник с номером {debtor_index}")
    debt = int(input("Сколько должны? "))
    total_debt += debt

print(f"Общая сумма долга: {total_debt}")
