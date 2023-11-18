class Point:
    x = 0
    y = 0
    color = 'black'


a = Point()
b = Point()
a.color = 'yellow'
print(a.__dict__)  # {'color': 'yellow'}
print(a.color)  # yellow
print(b.color)  # black
