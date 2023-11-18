class Point:
    pass


setattr(Point, 'color', 'black')
a = Point()
setattr(a, 'x', 0)
setattr(a, 'y', 0)
print(Point.color)  # black
print(a.x)  # 0
print(a.y)  # 0
