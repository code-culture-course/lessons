"""
Мини-проект Шаг 5: Полная версия с обработкой ошибок

Что мы изучаем:
- Обработка некорректных JSON файлов
- Валидация пользовательского ввода
- Корректное восстановление после ошибок
- Создание надёжной программы

Это финальная, готовая к продакшену версия.
"""

import json

TASKS_FILE = "tasks.json"

# Глобальный список для хранения задач
tasks = []


def load_tasks():
    """
    Загрузить задачи из JSON файла с обработкой ошибок.
    Возвращает True если успешно, False иначе.
    """
    global tasks
    try:
        file = open(TASKS_FILE, "r")
        tasks = json.load(file)
        file.close()
        
        # Проверить что tasks это список
        if not isinstance(tasks, list):
            print("Предупреждение: Неверный формат файла задач. Начинаем с чистого листа.")
            tasks = []
            return False
        
        print(f"Загружено {len(tasks)} задач(и) из файла.")
        return True
        
    except FileNotFoundError:
        print("Сохранённых задач не найдено. Начинаем с чистого листа.")
        tasks = []
        return True
        
    except json.JSONDecodeError:
        print("Предупреждение: Файл задач повреждён. Начинаем с чистого листа.")
        print("Старый файл будет сохранён как tasks.json.bak")
        # Сделать резервную копию повреждённого файла
        try:
            file = open(TASKS_FILE, "r")
            content = file.read()
            file.close()
            
            backup = open(TASKS_FILE + ".bak", "w")
            backup.write(content)
            backup.close()
        except:
            pass  # Если резервное копирование не удалось, просто продолжить
        
        tasks = []
        return False


def save_tasks():
    """Сохранить все задачи в JSON файл с обработкой ошибок."""
    try:
        file = open(TASKS_FILE, "w")
        json.dump(tasks, file, indent=2, ensure_ascii=False)
        file.close()
        return True
    except Exception as e:
        print(f"Ошибка сохранения задач: {e}")
        return False


def display_menu():
    """Показать опции меню."""
    print()
    print("=" * 40)
    print("МЕНЕДЖЕР СПИСКА ЗАДАЧ")
    print("=" * 40)
    print("1. Просмотреть задачи")
    print("2. Добавить задачу")
    print("3. Отметить задачу выполненной")
    print("4. Удалить задачу")
    print("5. Выход")
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
    """Добавить новую задачу с валидацией."""
    description = input("\nВведите описание задачи: ")
    
    # Валидация ввода
    if not description.strip():
        print("Задача не может быть пустой.")
        return
    
    if len(description) > 200:
        print("Описание задачи слишком длинное (макс 200 символов).")
        return
    
    # Создать словарь задачи
    task = {
        "description": description,
        "completed": False
    }
    
    tasks.append(task)
    
    if save_tasks():
        print(f"✓ Задача добавлена и сохранена!")
    else:
        print("✓ Задача добавлена (но сохранение не удалось - попробуем снова позже)")


def complete_task():
    """Отметить задачу как выполненную с валидацией."""
    view_tasks()
    if len(tasks) == 0:
        return
    
    try:
        choice = int(input("\nВведите номер задачи для отметки: "))
        
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            if save_tasks():
                print("✓ Задача отмечена как выполненная!")
            else:
                print("Задача обновлена но сохранение не удалось.")
        else:
            print(f"Пожалуйста, введите число от 1 до {len(tasks)}.")
            
    except ValueError:
        print("Пожалуйста, введите валидное число.")


def delete_task():
    """Удалить задачу с валидацией."""
    view_tasks()
    if len(tasks) == 0:
        return
    
    try:
        choice = int(input("\nВведите номер задачи для удаления: "))
        
        if 1 <= choice <= len(tasks):
            deleted = tasks.pop(choice - 1)
            if save_tasks():
                print(f"✓ Удалено: {deleted['description']}")
            else:
                # Восстановить задачу если сохранение не удалось
                tasks.insert(choice - 1, deleted)
                print("Удаление не удалось - не удалось сохранить изменения.")
        else:
            print(f"Пожалуйста, введите число от 1 до {len(tasks)}.")
            
    except ValueError:
        print("Пожалуйста, введите валидное число.")


# Инициализация программы
print("=" * 40)
print("МЕНЕДЖЕР СПИСКА ЗАДАЧ")
print("=" * 40)
print()

if not load_tasks():
    print("Начинаем с пустого списка задач.")

# Главный цикл программы
running = True
while running:
    display_menu()
    choice = input("\nВыберите опцию (1-5): ").strip()
    
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("\nДо свидания!")
        running = False
    else:
        print("\nНеверный выбор. Пожалуйста, выберите 1-5.")

print("Спасибо за использование Менеджера списка задач!")

"""
ПОЧЕМУ ЭТО ВАЖНО:

Эта версия корректно обрабатывает ошибки:
- Повреждённые JSON файлы → резервная копия и перезапуск
- Некорректный ввод → пользователь запрашивается снова
- Неудачи сохранения → пользователь уведомляется
- Пустые задачи → предотвращены

Надёжная программа предвидит проблемы и обрабатывает их без
сбоев. Это делает разницу между игрушечной программой и
готовым к продакшену инструментом.

Ключевые уроки:
1. Всегда валидируйте пользовательский ввод
2. Обрабатывайте файловые операции с try/except
3. Предоставляйте чёткие сообщения об ошибках
4. Делайте резервные копии важных данных перед перезаписью
5. Тестируйте крайние случаи (пустой ввод, некорректные числа, повреждённые файлы)
"""
