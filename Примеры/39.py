class Point:
    x = 0
    y = 0
    color = 'black'


Point.color = 'red'
Point.size = 5
print(Point.__dict__)
