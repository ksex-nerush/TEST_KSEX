try:
    numbers1 = int(input("Введи первое число на сложение: "))
    numbers2 = int(input("А теперь введи второе число на сложение: "))
    numbers3 = int(input("Введи первое число на вычитание: "))
    numbers4 = int(input("А теперь введи второе число на вычитание: "))
    numbers5 = int(input("Введи первое число на умножение: "))
    numbers6 = int(input("А теперь введи второе число на умножение: "))
    numbers7 = int(input("Введи первое число на деление: "))
    numbers8 = int(input("А теперь введи второе число на деление: "))

    result1 = numbers1 + numbers2
    result2 = numbers3 - numbers4
    result3 = numbers5 * numbers6
    result4 = numbers7 / numbers8
except ValueError:
    print("Товарищ! Это не число!")
except ZeroDivisionError:
    print("Вас в школе не учили, что на ноль делить нельзя??")
else:
    print(f"Сумма сложения: {result1}", f"Сумма вычитания: {result2}", f"Сумма умножения: {result3}", f"Сумма деления: {result4}", sep = "\n")

