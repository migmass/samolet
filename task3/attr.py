attr_name = input("Введте имя атрибута: ")
default_value = "Неизвестно"
value = getattr( person, attr_name, default_value)
print(f'Значение атрибута {attr_name}: {value}')