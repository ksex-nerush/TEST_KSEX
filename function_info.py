def show_info_object(object):
    try:
        return f"тип {type(object)}, длина {len(object)}"
    except TypeError as ex:
        return f"ОШИБКА! Объект не может являться цифрой. Введите другой тип значения! Подробности ошибки: {ex}"
    except Exception as ex:
        return f"НЕПРЕДВИДИМАЯ ОШИБКА: {ex.__class__}! Подробности ошибки: {ex}"


print(show_info_object("строка"))
print(show_info_object([2, 5, 7, 7]))
print(show_info_object((2, 5, 7, 7)))
print(show_info_object({2, 5, 7, 7}))
print(show_info_object({"a": 1, "b": 2, "c": 3}))
