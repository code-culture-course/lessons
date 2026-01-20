"""
Тестируемый менеджер задач

Демонстрирует, как структурировать I/O код для тестирования.

Ключевые принципы:
- Логика в чистых функциях (без I/O)
- I/O в тонких функциях-обёртках
- Чистые функции легко тестировать
"""

import json


# ============================================================
# ЧИСТЫЕ ФУНКЦИИ ЛОГИКИ (Легко тестировать)
# ============================================================

def validate_task_description(description):
    """
    Проверяет, валидно ли описание задачи.
    
    Аргументы:
        description: Строка с описанием задачи
        
    Возвращает:
        bool: True если валидно, False в противном случае
    """
    if not isinstance(description, str):
        return False
    return len(description.strip()) > 0


def create_task_dict(description):
    """
    Создаёт словарь задачи из описания.
    
    Аргументы:
        description: Строка с описанием задачи
        
    Возвращает:
        dict: Словарь задачи с описанием и статусом выполнения
    """
    return {
        "description": description.strip(),
        "completed": False
    }


def add_task(tasks, description):
    """
    Добавляет задачу в список, если она валидна.
    
    Аргументы:
        tasks: Список словарей задач
        description: Строка с описанием задачи
        
    Возвращает:
        bool: True если добавлена, False если невалидна
    """
    if not validate_task_description(description):
        return False
    
    task = create_task_dict(description)
    tasks.append(task)
    return True


def get_task_by_index(tasks, index):
    """
    Получает задачу по её индексу (начиная с 1).
    
    Аргументы:
        tasks: Список словарей задач
        index: Индекс начиная с 1
        
    Возвращает:
        dict or None: Словарь задачи или None если индекс невалиден
    """
    if not isinstance(index, int) or index < 1 or index > len(tasks):
        return None
    return tasks[index - 1]


def complete_task(tasks, index):
    """
    Отмечает задачу как выполненную.
    
    Аргументы:
        tasks: Список словарей задач
        index: Индекс начиная с 1
        
    Возвращает:
        bool: True если успешно, False если индекс невалиден
    """
    task = get_task_by_index(tasks, index)
    if task is None:
        return False
    
    task["completed"] = True
    return True


def delete_task(tasks, index):
    """
    Удаляет задачу из списка.
    
    Аргументы:
        tasks: Список словарей задач
        index: Индекс начиная с 1
        
    Возвращает:
        bool: True если удалена, False если индекс невалиден
    """
    if not isinstance(index, int) or index < 1 or index > len(tasks):
        return False
    
    tasks.pop(index - 1)
    return True


def format_task_list(tasks):
    """
    Форматирует задачи как список строк для отображения.
    
    Аргументы:
        tasks: Список словарей задач
        
    Возвращает:
        list: Отформатированные строки для каждой задачи
    """
    if len(tasks) == 0:
        return ["Задач пока нет."]
    
    lines = []
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else " "
        lines.append(f"{i}. [{status}] {task['description']}")
    return lines


# ============================================================
# ФУНКЦИИ ФАЙЛОВОГО I/O (Используют чистые функции выше)
# ============================================================

def load_tasks_from_file(filename):
    """
    Загружает задачи из JSON файла.
    
    Аргументы:
        filename: Путь к JSON файлу
        
    Возвращает:
        list: Список словарей задач, или пустой список при ошибке
    """
    try:
        file = open(filename, "r", encoding="utf-8")
        tasks = json.load(file)
        file.close()
        
        # Проверяем, что это список
        if not isinstance(tasks, list):
            return []
        
        return tasks
        
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks_to_file(filename, tasks):
    """
    Сохраняет задачи в JSON файл.
    
    Аргументы:
        filename: Путь к JSON файлу
        tasks: Список словарей задач
        
    Возвращает:
        bool: True если успешно, False в противном случае
    """
    try:
        file = open(filename, "w", encoding="utf-8")
        json.dump(tasks, file, indent=2, ensure_ascii=False)
        file.close()
        return True
    except Exception:
        return False


# ============================================================
# ФУНКЦИИ КОНСОЛЬНОГО I/O (Тонкие обёртки)
# ============================================================

def display_tasks(tasks):
    """Отображает все задачи в консоли."""
    print("\nВаши задачи:")
    for line in format_task_list(tasks):
        print(f"  {line}")


def get_task_input():
    """Получает описание задачи от пользователя."""
    return input("\nВведите описание задачи: ")


def get_task_number(prompt):
    """
    Получает номер задачи от пользователя.
    
    Аргументы:
        prompt: Приглашение для отображения
        
    Возвращает:
        int or None: Номер, или None если невалидно
    """
    try:
        return int(input(prompt))
    except ValueError:
        return None


# ============================================================
# ОСНОВНАЯ ПРОГРАММА (Слой I/O)
# ============================================================

def main():
    """Основная программа - оркестрация I/O."""
    TASKS_FILE = "tasks.json"
    
    print("=" * 40)
    print("МЕНЕДЖЕР ЗАДАЧ")
    print("=" * 40)
    
    tasks = load_tasks_from_file(TASKS_FILE)
    print(f"\nЗагружено {len(tasks)} задач(и).")
    
    running = True
    while running:
        print("\n" + "=" * 40)
        print("1. Просмотреть задачи")
        print("2. Добавить задачу")
        print("3. Выполнить задачу")
        print("4. Удалить задачу")
        print("5. Выйти")
        print("=" * 40)
        
        choice = input("\nВыберите опцию: ").strip()
        
        if choice == "1":
            display_tasks(tasks)
            
        elif choice == "2":
            description = get_task_input()
            if add_task(tasks, description):
                save_tasks_to_file(TASKS_FILE, tasks)
                print("✓ Задача добавлена!")
            else:
                print("✗ Задача не может быть пустой.")
                
        elif choice == "3":
            display_tasks(tasks)
            if len(tasks) > 0:
                number = get_task_number("\nНомер задачи для выполнения: ")
                if number and complete_task(tasks, number):
                    save_tasks_to_file(TASKS_FILE, tasks)
                    print("✓ Задача выполнена!")
                else:
                    print("✗ Неверный номер задачи.")
                    
        elif choice == "4":
            display_tasks(tasks)
            if len(tasks) > 0:
                number = get_task_number("\nНомер задачи для удаления: ")
                if number and delete_task(tasks, number):
                    save_tasks_to_file(TASKS_FILE, tasks)
                    print("✓ Задача удалена!")
                else:
                    print("✗ Неверный номер задачи.")
                    
        elif choice == "5":
            print("\nДо свидания!")
            running = False
            
        else:
            print("\nНеверный выбор.")
    
    save_tasks_to_file(TASKS_FILE, tasks)


if __name__ == "__main__":
    main()
