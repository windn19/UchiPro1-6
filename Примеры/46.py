class Point:
    x = 0
    y = 0
    color = 'black'


a = Point()
a.size = 10
delattr(a, 'size')
delattr(Point, 'color')
print(a.__dict__)  # {}
print(Point.color)  # ошибка AttributeError
