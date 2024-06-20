def calculate_compound_interest(principal, rate, years):
    amount = principal * (1 + rate) ** years
    return amount

principal = float(input("Введите начальную сумму: "))
rate = float(input("Введите процентную ставку (в виде десятичной дроби): "))
years = int(input("Введите количество лет: "))

final_amount = calculate_compound_interest(principal, rate, years)
print(f"Через {years} лет ваша инвестиция вырастет до: {final_amount:.2f}")

