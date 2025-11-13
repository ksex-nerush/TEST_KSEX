def multiply (a: int, b: int):
    try:
        return a * b
    except TypeError as ex:
        return f"ОШИБКА! Аргументы не являются цифрами. Введите числовые значения! Подробности ошибки: {ex}"
    except Exception as ex:
        return f"НЕПРЕДВИДИМАЯ ОШИБКА: {ex.__class__}! Подробности ошибки: {ex}"


result = multiply(6, 8)
print(result)
result = multiply("dwdwdwd", "mmmmmm")
print(result)
result = multiply("6", 8)
print(result)
