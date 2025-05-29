### Задача 4. Класс Book
# Атрибуты: title, author, pages
# __str__ — вывод строки "<title> by <author>, <pages> pages"
# Спец. методы: __eq__, __lt__ — сравнение по страницам

class Book:
    pass

# Тесты
b1 = Book("1984", "Orwell", 300)
b2 = Book("Animal Farm", "Orwell", 200)
b3 = Book("Brave New World", "Huxley", 300)
assert str(b1) == '"1984" by Orwell, 300 pages'
assert b1 == b3
assert b2 < b1
