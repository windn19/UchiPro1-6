class Point:
    x = 0
    y = 0
    color = 'black'


a = Point()
print(getattr(Point, 'color'))  # black
print(getattr(Point, 'color', 'Нет такого атрибута'))  # black
print(getattr(Point, 'size', 'Нет такого атрибута'))  # Нет такого атрибута
print(getattr(a, 'color', 'Нет такого атрибута'))  # black
print(getattr(a, 'size'))  # ошибка AttributeError
