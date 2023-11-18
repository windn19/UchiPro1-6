class Point:
    pass


a = Point()
b = Point()
print(type(a))  # <class '__main__.Point'>
print(isinstance(a, Point))  # True
print(id(a), id(b))  # 2931410058880 2931410054464
