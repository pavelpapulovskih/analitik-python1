def average_age(employees):
 valid_ages = [age for name, age in employees if age >= 0]
 return sum(valid_ages) / len(valid_ages) if valid_ages else 0
employees = [("Alice", 30), ("Bob", -5), ("Charlie", 40)]
print(average_age(employees)) # Вывод: 35.0