def show_info_object(object):
    return f"тип {type(object)}, длина {len(object)}"

print(show_info_object("строка"))
print(show_info_object([2, 5, 7, 7]))
print(show_info_object((2, 5, 7, 7)))
print(show_info_object({2, 5, 7, 7}))
print(show_info_object({"a": 1, "b": 2, "c": 3}))
