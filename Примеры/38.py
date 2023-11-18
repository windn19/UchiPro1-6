class Point:
    x = 0
    y = 0
    color = 'black'


a = Point()
b = Point()
print(a.color, b.color)  # black black
Point.color = 'red'
print(a.color, b.color)  # red red
