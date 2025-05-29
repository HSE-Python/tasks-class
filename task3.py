### Задача 3. Класс BankAccount
# Атрибуты: owner (строка), balance (число)
# Методы: deposit(amount), withdraw(amount)
# Спец. методы: __eq__, __lt__ — сравнение по балансу

class BankAccount:
    pass

# Тесты
acc1 = BankAccount("Tom", 100)
acc2 = BankAccount("Jerry", 150)
acc1.deposit(50)
assert acc1.balance == 150
assert acc1 == acc2
acc1.withdraw(70)
assert acc1.balance == 80
assert acc1 < acc2