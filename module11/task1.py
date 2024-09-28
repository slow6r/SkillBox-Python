euro_to_dollar = 1.25
dollar_to_ruble = 60.87

euros = float(input("Введите стоимость покупки в евро: "))
dollars = euros * euro_to_dollar
rubles = dollars * dollar_to_ruble

print(f"{euros} евро = {rubles:.2f} рублей.")
