class Student:
    statuses = {1: 'primary',
                2: 'primary',
                3: 'primary',
                4: 'primary',
                5: 'middle',
                6: 'middle',
                7: 'middle',
                8: 'middle',
                9: 'middle',
                10: 'high',
                11: 'high'}
    max_course = 11


students = []

n = int(input())
for i in range(n):
    name, course = input().split(', ')
    student = Student()
    student.name = name
    student.course = int(course)
    students.append(student)

for student in students:
    student.course = student.course + 1 if student.course < 11 else None
    print(f'{student.name}, {student.course}, {Student.statuses.get(student.course)}')

