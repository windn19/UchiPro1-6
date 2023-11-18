class Point:
    x = 0
    y = 0
    color = 'black'


a = Point()
b = Point()
a.x, a.y = 1, 2
b.color = 'green'
print(a.x, a.y)  # 1 2
print(a.color)  # black
print(b.x, b.y)  # 0 0
print(b.color)  # green
