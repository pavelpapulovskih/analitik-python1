def normalize_grades(grades):
 valid_grades = [grade for grade in grades if grade >= 0]
 return sorted(valid_grades, reverse=True)
# Пример использования
grades = [95, -10, 82, 90, -5, 77]
print(normalize_grades(grades)) # Вывод: [95, 90, 82, 77]