import heapq

class TaskQueue:
    def __init__(self):
        self.queue = []  # Очередь з пріоритетами
        self.completed_tasks_list = []  # Список виконаних задач

    def enqueue(self, id, name, priority):
        # Додаємо завдання до черги з пріоритетом
        # Використовуємо протилежний пріоритет, щоб задачі з більшим пріоритетом були першими
        heapq.heappush(self.queue, (-priority, id, name))

    def dequeue(self):
        if not self.is_empty():
            # Видаляємо та повертаємо завдання з найвищим пріоритетом
            priority, id, name = heapq.heappop(self.queue)
            # Додаємо завдання до списку виконаних
            self.completed_tasks_list.append((id, name, -priority))
            return id, name, -priority
        else:
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def completed_tasks(self):
        return self.completed_tasks_list


task_queue = TaskQueue()

task_queue.enqueue(1, "Підготувати звіт про продажі", 3)
task_queue.enqueue(2, "Відправити заказ клієнту A", 1)
task_queue.enqueue(3, "Сформувати презентацію для команди", 3)
task_queue.enqueue(4, "Зателефонувати постачальнику щодо поставки товару", 2)
task_queue.enqueue(5, "Відправити заказ клієнту B", 1)
task_queue.enqueue(6, "Замовити нове обладнання для офісу", 2)

while not task_queue.is_empty():
    id, name, priority = task_queue.dequeue()
    print(f"Виконую завдання {id}: {name} (пріоритет {priority})")

completed_tasks = task_queue.completed_tasks()
print("\nВиконані завдання:")
for id, name, priority in completed_tasks:
    print(f"№{id}: {name} (пріоритет {priority})")







