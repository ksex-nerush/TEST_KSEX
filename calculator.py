# сложение
try:
    numbers1 = int(input("Введи первое число на сложение: "))
    numbers2 = int(input("А теперь введи второе число на сложение: "))
    result = numbers1 + numbers2
except ValueError:
    print("Товарищ! Это не число!")
else:
    print(f"Сумма сложения: {result}")

# вычитание
try:
    numbers1 = int(input("Введи первое число на вычитание: "))
    numbers2 = int(input("А теперь введи второе число на вычитание: "))
    result = numbers1 - numbers2
except ValueError:
    print("Товарищ! Это не число!")
else:
    print(f"Сумма вычитания: {result}")

# умножение
try:
    numbers1 = int(input("Введи первое число на умножение: "))
    numbers2 = int(input("А теперь введи второе число на умножение: "))
    result = numbers1 * numbers2
except ValueError:
    print("Товарищ! Это не число!")
else:
    print(f"Сумма умножения: {result}")

# деление
try:
    numbers1 = int(input("Введи первое число на деление: "))
    numbers2 = int(input("А теперь введи второе число на деление: "))
    result = numbers1 / numbers2
except ValueError:
    print("Товарищ! Это не число!")
except ZeroDivisionError:
    print("Вас в школе не учили, что на ноль делить нельзя??")
else:
    print(f"Сумма деления: {result}")
