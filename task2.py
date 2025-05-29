### Задача 2. Класс Student
# Атрибуты: name, grades (список)
# Методы: add_grade(grade), average()

class Student:
    pass

# Тесты
s = Student("Alice")
s.add_grade(4)
s.add_grade(5)
s.add_grade(3)
assert s.grades == [4, 5, 3]
assert round(s.average(), 2) == 4.0