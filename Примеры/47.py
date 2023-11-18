class Point:
    x = 0
    y = 0
    color = 'black'


a = Point()
a.size = 10
print(hasattr(Point, 'color'))  # True
print(hasattr(Point, 'size'))  # False
print(hasattr(a, 'size'))  # True
