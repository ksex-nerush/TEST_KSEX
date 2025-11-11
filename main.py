try:
    number1 = int(input("Введи число: "))
    number2 = int(input("И еще раз число: "))
    result = number1 / number2
except ValueError:
    print("Товарищ! Это не число!")
except ZeroDivisionError:
    print("Вас в школе не учили, что на ноль делить нельзя??")
else:
    print(f"Поделили и получилось: {result}")
finally:
    print("ВОТ И ВСЕ! ПОКА!")