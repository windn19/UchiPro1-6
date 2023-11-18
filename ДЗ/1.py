# 9. Напиши программу, в которой создай класс Task. Добавь атрибуты классу:
#     • id = 0
#     • name = 'task'
#     • category_id = None
# Создай экземпляр этого класса и у него измени: id на 1, имя (name) на 'new_task', category_id на 0.
# Используя специальную переменную __dict__ , выведи на экран все атрибуты объекта.
#
# Выходные данные:
# Выводится все атрибуты объекта.


class Task:
    id = 0
    name = 'task'
    category_id = None


task = Task()
task.id = 1
task.name = 'new_task'
task.category_id = 0
print(task.__dict__)
