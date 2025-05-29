### Задача 1. Класс Rectangle
# Атрибуты: width, height
# Методы: area(), perimeter()
# Специальные методы: __eq__, __lt__ — сравнение по площади

class Rectangle:
    def __init__(self, width, height):
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass

# Тесты
r1 = Rectangle(2, 3)
r2 = Rectangle(3, 2)
r3 = Rectangle(1, 6)
assert r1.area() == 6
assert r1.perimeter() == 10
assert r1 == r2
assert r3 < r1