class Point:
    x = 0
    y = 0
    color = 'black'


print(Point.x, Point.y)  # 0 0
print(Point.color)  # black
print(Point.__dict__)
# {'__module__': '__main__', 'x': 0, 'y': 0, 'color': 'black', ...}
