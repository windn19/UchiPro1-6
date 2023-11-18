class Point:
    x = 0
    y = 0
    color = 'black'


a = Point()
b = Point()
print(a.color)  # black
print(b.x, b.y)  # 0 0
print(a.__dict__)  # {}
print(b.__dict__)  # {}
