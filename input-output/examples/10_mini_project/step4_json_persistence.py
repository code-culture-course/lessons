"""
Мини-проект Шаг 4: Сохранение JSON

Что мы изучаем:
- Использование JSON для структурированных данных
- Хранение больше чем просто строк
- Лучший формат данных для будущего расширения

Теперь мы можем легко добавить больше полей к задачам (например, статус 'выполнено').
"""

import json

TASKS_FILE = "tasks.json"

# Глобальный список для хранения задач
# Теперь каждая задача - словарь с несколькими полями
tasks = []


def load_tasks():
    """Загрузить задачи из JSON файла если он существует."""
    global tasks
    try:
        file = open(TASKS_FILE, "r")
        tasks = json.load(file)
        file.close()
        print(f"Загружено {len(tasks)} задач(и) из файла.")
    except FileNotFoundError:
        print("Сохранённых задач не найдено. Начинаем с чистого листа.")


def save_tasks():
    """Сохранить все задачи в JSON файл."""
    file = open(TASKS_FILE, "w")
    json.dump(tasks, file, indent=2, ensure_ascii=False)
    file.close()


def display_menu():
    """Показать опции меню."""
    print()
    print("=" * 40)
    print("МЕНЕДЖЕР СПИСКА ЗАДАЧ")
    print("=" * 40)
    print("1. Просмотреть задачи")
    print("2. Добавить задачу")
    print("3. Отметить задачу выполненной")
    print("4. Выход")
    print("=" * 40)


def view_tasks():
    """Отобразить все задачи со статусом выполнения."""
    print()
    if len(tasks) == 0:
        print("Задач пока нет. Добавьте несколько!")
    else:
        print("Ваши задачи:")
        for i, task in enumerate(tasks, 1):
            status = "✓" if task["completed"] else " "
            print(f"  {i}. [{status}] {task['description']}")


def add_task():
    """Добавить новую задачу и сохранить в файл."""
    description = input("\nВведите описание задачи: ")
    if description.strip():
        # Создать словарь задачи
        task = {
            "description": description,
            "completed": False
        }
        tasks.append(task)
        save_tasks()
        print(f"✓ Задача добавлена и сохранена!")
    else:
        print("Задача не может быть пустой.")


def complete_task():
    """Отметить задачу как выполненную."""
    view_tasks()
    if len(tasks) == 0:
        return
    
    try:
        choice = int(input("\nВведите номер задачи для отметки: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            save_tasks()
            print("✓ Задача отмечена как выполненная!")
        else:
            print("Неверный номер задачи.")
    except ValueError:
        print("Пожалуйста, введите валидное число.")


# Загрузить задачи при запуске
print("Добро пожаловать в Менеджер списка задач!")
load_tasks()

# Главный цикл программы
running = True
while running:
    display_menu()
    choice = input("\nВыберите опцию (1-4): ")
    
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        print("\nДо свидания!")
        running = False
    else:
        print("\nНеверный выбор. Пожалуйста, выберите 1-4.")

print("Спасибо за использование Менеджера списка задач!")

"""
ПОЧЕМУ ЭТО ВАЖНО:

JSON позволяет нам легко хранить структурированные данные. Каждая задача теперь
словарь с несколькими полями. Мы можем добавить больше полей позже
(например, 'приоритет', 'срок') не ломая существующий код.

JSON файл также читаем для человека и может быть разделён с другими
программами или языками программирования.

Но нам всё ещё не хватает обработки ошибок. Что если JSON файл
повреждается? Это финальный шаг!
"""
