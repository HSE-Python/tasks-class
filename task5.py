### Задача 5. Класс Date
# Атрибуты: year, month, day
# Спец. методы: __eq__, __lt__, __gt__ — сравнение по календарю

class Date:
    pass

# Тесты
d1 = Date(2023, 5, 10)
d2 = Date(2023, 5, 12)
d3 = Date(2023, 5, 10)
assert d1 < d2
assert d2 > d1
assert d1 == d3